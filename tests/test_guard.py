"""Tests for the tutor's keys guard, tutor/.claude/hooks/keys_guard.py.

Each test writes a sample PreToolUse hook input to the script's stdin and
checks its exit code: 2 means blocked, 0 means allowed. The inputs use a
temporary workspace with keys/, quizzes/ and lessons/ folders as their cwd,
so the Grep checks do not depend on this repo's own files.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUARD = os.path.join(REPO, "tutor", ".claude", "hooks", "keys_guard.py")

BLOCKED = 2
ALLOWED = 0


class GuardTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.ws = self._tmp.name
        for folder in ("keys", "quizzes", "lessons"):
            os.mkdir(os.path.join(self.ws, folder))
        with open(os.path.join(self.ws, "keys", "0001.json"), "w") as f:
            f.write('{"answer": "B"}')

    def tearDown(self):
        self._tmp.cleanup()

    def run_guard(self, tool_name, tool_input, agent_type=None, raw=None):
        if raw is None:
            data = {
                "hook_event_name": "PreToolUse",
                "tool_name": tool_name,
                "tool_input": tool_input,
                "cwd": self.ws,
            }
            if agent_type is not None:
                data["agent_type"] = agent_type
                data["agent_id"] = "agent-test-1"
            raw = json.dumps(data)
        result = subprocess.run(
            [sys.executable, GUARD],
            input=raw,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result

    def assertBlocked(self, result):
        self.assertEqual(result.returncode, BLOCKED, result.stderr)
        self.assertIn("keys guard", result.stderr)

    def assertAllowed(self, result):
        self.assertEqual(result.returncode, ALLOWED, result.stderr)

    # The main conversation's reads of keys/: blocked, one per tool.

    def test_main_read_key_blocked(self):
        self.assertBlocked(self.run_guard("Read", {"file_path": "keys/0001.json"}))

    def test_main_read_key_absolute_path_blocked(self):
        path = os.path.join(self.ws, "keys", "0001.json")
        self.assertBlocked(self.run_guard("Read", {"file_path": path}))

    def test_main_read_key_dot_slash_blocked(self):
        self.assertBlocked(self.run_guard("Read", {"file_path": "./keys/0001.json"}))

    def test_main_read_key_backslash_blocked(self):
        self.assertBlocked(self.run_guard("Read", {"file_path": "keys\\0001.json"}))

    def test_main_grep_in_keys_blocked(self):
        self.assertBlocked(
            self.run_guard("Grep", {"pattern": "answer", "path": "keys"})
        )

    def test_main_grep_whole_workspace_blocked(self):
        # No path: Grep would search keys/ along with everything else.
        self.assertBlocked(self.run_guard("Grep", {"pattern": "answer"}))

    def test_main_glob_in_keys_blocked(self):
        self.assertBlocked(self.run_guard("Glob", {"pattern": "keys/*.json"}))

    def test_main_bash_cat_key_blocked(self):
        self.assertBlocked(self.run_guard("Bash", {"command": "cat keys/0001.json"}))

    def test_main_powershell_get_content_key_blocked(self):
        self.assertBlocked(
            self.run_guard("PowerShell", {"command": "Get-Content keys/0001.json"})
        )

    # Subagents: the grader may read keys/, others may not.

    def test_grader_read_key_allowed(self):
        self.assertAllowed(
            self.run_guard("Read", {"file_path": "keys/0001.json"}, agent_type="grader")
        )

    def test_grader_bash_cat_key_allowed(self):
        self.assertAllowed(
            self.run_guard("Bash", {"command": "cat keys/0001.json"}, agent_type="grader")
        )

    def test_other_subagent_read_key_blocked(self):
        self.assertBlocked(
            self.run_guard(
                "Read", {"file_path": "keys/0001.json"}, agent_type="quiz-reviewer"
            )
        )

    # The main conversation's other reads: still allowed.

    def test_main_read_quiz_allowed(self):
        self.assertAllowed(self.run_guard("Read", {"file_path": "quizzes/0001.json"}))

    def test_main_read_mission_allowed(self):
        self.assertAllowed(self.run_guard("Read", {"file_path": "MISSION.md"}))

    def test_main_bash_ls_lessons_allowed(self):
        self.assertAllowed(self.run_guard("Bash", {"command": "ls lessons"}))

    def test_main_grep_in_lessons_allowed(self):
        self.assertAllowed(
            self.run_guard("Grep", {"pattern": "agent", "path": "lessons"})
        )

    def test_main_glob_lessons_allowed(self):
        self.assertAllowed(self.run_guard("Glob", {"pattern": "lessons/*.html"}))

    def test_unguarded_tool_allowed(self):
        self.assertAllowed(
            self.run_guard("Write", {"file_path": "NOTES.md", "content": "hi"})
        )

    # Input it cannot read: blocked on purpose rather than crashing.

    def test_unreadable_input_blocked(self):
        self.assertBlocked(self.run_guard(None, None, raw="not json"))


if __name__ == "__main__":
    unittest.main()
