"""Tests for handlers/decorators.py — input_error decorator."""

from decorators import input_error


class TestInputError:
    def test_success_passthrough(self) -> None:
        @input_error
        def ok(*_args):
            return "result"

        assert ok() == "result"

    def test_passes_args(self) -> None:
        @input_error
        def echo(a, b):
            return f"{a}-{b}"

        assert echo("x", "y") == "x-y"

    def test_catches_value_error(self) -> None:
        @input_error
        def bad(*_args):
            raise ValueError

        assert bad() == "Give me correct arguments please."

    def test_catches_index_error(self) -> None:
        @input_error
        def bad(*_args):
            raise IndexError

        assert bad() == "Enter the required arguments."

    def test_catches_key_error(self) -> None:
        @input_error
        def bad(*_args):
            raise KeyError("x")

        assert bad() == "Contact not found."

    def test_does_not_catch_type_error(self) -> None:
        @input_error
        def bad(*_args):
            raise TypeError("oops")

        import pytest

        with pytest.raises(TypeError, match="oops"):
            bad()

    def test_does_not_catch_runtime_error(self) -> None:
        @input_error
        def bad(*_args):
            raise RuntimeError

        import pytest

        with pytest.raises(RuntimeError):
            bad()

    def test_value_error_with_message_still_returns_generic(self) -> None:
        @input_error
        def bad(*_args):
            raise ValueError("specific message")

        assert bad() == "Give me correct arguments please."

    def test_key_error_message_ignored(self) -> None:
        @input_error
        def bad(*_args):
            raise KeyError("Alice")

        assert bad() == "Contact not found."

    def test_returns_none_when_func_returns_none(self) -> None:
        @input_error
        def noop(*_args):
            return None

        assert noop() is None
