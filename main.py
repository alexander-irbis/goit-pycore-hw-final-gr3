import shlex

from cli import colors as c
from cli.commands import default_commands, handle_help, handle_quit

TITLE = "Assistant Bot"
TEAM_NAME = "Team #3"
TEAM_MEMBERS = [
    "Olga Shadrunova",
    "Maks Kaniuka",
    "Ivan Bochkarov",
    "Oleksandr Semychenkov",
]


def format_title(title: str) -> str:
    """Format title in a Unicode box with shadow."""
    width = len(title) + 4
    box = "═" * width
    shadow_line = "░" * (width + 2)
    return (
        f"  {c.TITLE}╔{box}╗{c.RESET}\n"
        f"  {c.TITLE}║  {title}  ║{c.RESET}{c.SHADOW}░{c.RESET}\n"
        f"  {c.TITLE}╚{box}╝{c.RESET}{c.SHADOW}░{c.RESET}\n"
        f"   {c.SHADOW}{shadow_line}{c.RESET}"
    )


def format_team(name: str, members: list[str]) -> str:
    """Format team block with members listed."""
    lines = [f"  {c.TEAM}{name}:{c.RESET}"]
    for member in members:
        lines.append(f"    {c.BULLET}●{c.RESET} {member}")
    return "\n".join(lines)


def main() -> None:
    commands = default_commands()

    print()
    print(format_title(TITLE))
    print()
    print(format_team(TEAM_NAME, TEAM_MEMBERS))
    print()
    print(handle_help(commands))
    print()

    while True:
        try:
            user_input = input(">>> ").strip()
        except EOFError, KeyboardInterrupt:
            print()
            print(f"{c.FAREWELL}{handle_quit()}{c.RESET}")
            break

        if not user_input:
            continue

        try:
            parts = shlex.split(user_input)
        except ValueError:
            print(f"{c.ERROR}Invalid input: unmatched quotes.{c.RESET}")
            continue

        cmd_name = parts[0].lower()

        if cmd_name in ("quit", "exit", "close"):
            print(f"{c.FAREWELL}{handle_quit()}{c.RESET}")
            break

        if cmd_name == "help":
            print(f"\n{handle_help(commands)}\n")
            continue

        handler = commands.get(cmd_name)
        if handler is None:
            print(f"{c.ERROR}Unknown command: {cmd_name}{c.RESET}")
            continue

        try:
            result = handler(*parts[1:])
        except ValueError as exc:
            print(f"\n  {c.ERROR}Invalid input: {exc}{c.RESET}")
            print(f"  {c.USAGE}Usage: {cmd_name} — {handler.__doc__}{c.RESET}\n")
            continue

        print(f"\n{result}\n")


if __name__ == "__main__":
    main()
