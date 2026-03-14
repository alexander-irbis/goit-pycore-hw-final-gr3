from collections.abc import Callable
from typing import Any

from cli import colors as c


def command(help_text: str) -> Callable[[Callable], Callable]:
    """Decorator that wraps a function and sets help_text as the wrapper's docstring."""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        wrapper.__doc__ = help_text
        return wrapper

    return decorator


@command("Show available commands.")
def handle_help(commands: dict[str, Callable]) -> str:
    """Format and return a help listing of all registered commands."""
    lines = [f"  {c.HEADER}Available commands:{c.RESET}"]
    for name, handler in sorted(commands.items()):
        colored_name = f"{c.CMD_NAME}{name:<15}{c.RESET}"
        colored_desc = f"{c.CMD_DESC}{handler.__doc__}{c.RESET}"
        lines.append(f"    {colored_name} {colored_desc}")
    return "\n".join(lines)


@command("Echo arguments back (test command).")
def handle_echo(*args: str) -> str:
    """Print all received arguments."""
    lines = [f"  {i}: {arg}" for i, arg in enumerate(args, 1)]
    return "\n".join(lines) if lines else "(no arguments)"


@command("Greet by name. Usage: greet <name>")
def handle_greet(*args: str) -> str:
    """Greet the given person."""
    if not args:
        raise ValueError("name is required")
    return f"  {c.GREETING}Hello, {args[0]}!{c.RESET}"


@command("Exit the assistant bot.")
def handle_quit() -> str:
    """Return a farewell message."""
    return f"{c.FAREWELL}Good bye!{c.RESET}"


def default_commands() -> dict[str, Callable]:
    """Default command registry."""
    return {
        "echo": handle_echo,
        "greet": handle_greet,
        "help": handle_help,
        "quit": handle_quit,
    }
