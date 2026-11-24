#!/usr/bin/env python3
"""PreToolUse guard: keep keys/ away from the tutor's main conversation.

Claude Code sends a JSON object on stdin with tool_name, tool_input, cwd and,
inside a subagent, agent_type. This script decides on purpose in every case:

- exit 0: the call goes ahead
- exit 2: the call is blocked, and the message on stderr goes to the model

Rules:
- A subagent whose agent_type is in ALLOWED_AGENTS may read keys/.
- Otherwise a Read, Grep, Glob, Bash or PowerShell call that names a path
  segment called "keys" is blocked.
- A Grep with no path, or a path whose folder directly holds keys/, is blocked
  too, because it would search the key's contents without naming keys/.
- Input that cannot be read as a JSON object is blocked.
"""

import json
import os
import re
import sys

ALLOWED_AGENTS = {"grader"}
GUARDED_TOOLS = {"Read", "Grep", "Glob", "Bash", "PowerShell"}

# "keys" as a whole path segment: preceded by the start, a slash, a backslash,
# whitespace, a quote, "=", "(" or ":", and followed by a slash, a backslash,
# the end, whitespace, a quote, ";", "|", "&", ")" or a glob character.
KEYS_SEGMENT = re.compile(r"""(?:^|[\s/\\"'=(:])keys(?:$|[\s/\\"';|&)*?\[{])""")

BLOCK_MESSAGE = (
    "Blocked by the tutor's keys guard: the answer keys in keys/ are not "
    "readable from the main conversation, so the tutor cannot hand out an "
    "answer. Grading that needs a key goes to the grader subagent. Read the "
    "quiz in quizzes/ or the lesson in lessons/ instead."
)

GREP_ROOT_MESSAGE = (
    "Blocked by the tutor's keys guard: this search would look inside keys/, "
    "which the main conversation may not read. Give Grep a path that does not "
    "contain keys/, such as lessons/ or quizzes/."
)


def block(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def strings_in(value):
    """Every string inside a tool_input value, however deeply nested."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings_in(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings_in(item)


def names_keys(text):
    return bool(KEYS_SEGMENT.search(text.replace("\\", "/")))


def grep_searches_keys(tool_input, cwd):
    """True when a Grep's folder directly holds a keys/ folder."""
    path = tool_input.get("path") or cwd or os.getcwd()
    if not isinstance(path, str):
        return True
    if not os.path.isabs(path) and cwd:
        path = os.path.join(cwd, path)
    return os.path.isdir(os.path.join(path, "keys"))


def main():
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        block("Blocked by the tutor's keys guard: it could not read its input.")
    if not isinstance(data, dict):
        block("Blocked by the tutor's keys guard: its input was not a JSON object.")

    if data.get("agent_type") in ALLOWED_AGENTS:
        sys.exit(0)

    tool = data.get("tool_name")
    if tool not in GUARDED_TOOLS:
        sys.exit(0)

    tool_input = data.get("tool_input")
    if not isinstance(tool_input, dict):
        block("Blocked by the tutor's keys guard: the tool input was not readable.")

    if any(names_keys(s) for s in strings_in(tool_input)):
        block(BLOCK_MESSAGE)

    if tool == "Grep":
        cwd = data.get("cwd") if isinstance(data.get("cwd"), str) else None
        if grep_searches_keys(tool_input, cwd):
            block(GREP_ROOT_MESSAGE)

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        block("Blocked by the tutor's keys guard: it hit an unexpected error.")
