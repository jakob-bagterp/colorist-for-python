# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.


def get_output(capfd: object) -> str:
    terminal_output, _ = capfd.readouterr()
    return terminal_output
