"""Tests for handlers/note_handlers.py — pure helper functions."""

from note_handlers import parse_note_input, show_note_help


class TestParseNoteInput:
    def test_simple_command(self) -> None:
        cmd, args = parse_note_input("add-note")
        assert cmd == "add-note"
        assert args == []

    def test_command_with_args(self) -> None:
        cmd, args = parse_note_input("add-note Title some content")
        assert cmd == "add-note"
        assert args == ["Title", "some", "content"]

    def test_lowercases_command(self) -> None:
        cmd, _args = parse_note_input("ADD-NOTE title")
        assert cmd == "add-note"

    def test_preserves_arg_case(self) -> None:
        _cmd, args = parse_note_input("find MyTitle")
        assert args == ["MyTitle"]

    def test_empty_string(self) -> None:
        cmd, args = parse_note_input("")
        assert cmd == ""
        assert args == []

    def test_whitespace_only(self) -> None:
        cmd, args = parse_note_input("   ")
        assert cmd == ""
        assert args == []

    def test_strips_leading_trailing_whitespace(self) -> None:
        cmd, args = parse_note_input("  add-note  title  ")
        assert cmd == "add-note"
        assert args == ["title"]

    def test_single_word(self) -> None:
        cmd, args = parse_note_input("all-notes")
        assert cmd == "all-notes"
        assert args == []


class TestShowNoteHelp:
    def test_returns_string(self) -> None:
        result = show_note_help()
        assert isinstance(result, str)

    def test_contains_all_commands(self) -> None:
        result = show_note_help()
        expected_commands = [
            "add-note",
            "change-note-title",
            "change-note-content",
            "remove-note-content",
            "delete-note",
            "add-tag",
            "remove-tag",
            "find-note-by-title",
            "find-notes-by-tag",
            "all-notes",
        ]
        for cmd in expected_commands:
            assert cmd in result, f"Missing command: {cmd}"

    def test_not_empty(self) -> None:
        assert len(show_note_help().strip()) > 0
