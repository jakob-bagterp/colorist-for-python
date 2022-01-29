def get_output(capfd: object) -> str:
    terminal_output, _ = capfd.readouterr()
    return terminal_output
