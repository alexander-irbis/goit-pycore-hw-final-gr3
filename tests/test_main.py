from main import main


def test_quit_command(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "quit")
    main()
    output = capsys.readouterr().out
    assert "Assistant Bot" in output
    assert "Good bye!" in output


def test_exit_command(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    main()
    output = capsys.readouterr().out
    assert "Good bye!" in output


def test_close_command(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "close")
    main()
    output = capsys.readouterr().out
    assert "Good bye!" in output


def test_help_then_quit(monkeypatch, capsys) -> None:
    inputs = iter(["help", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    output = capsys.readouterr().out
    # Help listing appears twice: on start and on "help" command
    assert output.count("Show available commands.") == 2


def test_unknown_command(monkeypatch, capsys) -> None:
    inputs = iter(["foobar", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    output = capsys.readouterr().out
    assert "Unknown command: foobar" in output


def test_eof_exits_gracefully(monkeypatch, capsys) -> None:
    def raise_eof(_: str) -> str:
        raise EOFError

    monkeypatch.setattr("builtins.input", raise_eof)
    main()
    output = capsys.readouterr().out
    assert "Good bye!" in output


def test_greeting_includes_help_listing(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "quit")
    main()
    output = capsys.readouterr().out
    lines = output.split("\n")
    assert lines[0] == "Assistant Bot"
    assert "help" in output
    assert "quit" in output
