from colorist import green, yellow, red, magenta, blue, cyan, white, black
import terminal

def test_green_full_text_color(capfd: object) -> None:
    text = "This is GREEN!"
    green(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[32m{text}\033[0m\n"

def test_yellow_full_text_color(capfd: object) -> None:
    text = "This is YELLOW!"
    yellow(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[33m{text}\033[0m\n"

def test_red_full_text_color(capfd: object) -> None:
    text = "This is RED!"
    red(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[31m{text}\033[0m\n"

def test_magenta_full_text_color(capfd: object) -> None:
    text = "This is MAGENTA!"
    magenta(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[35m{text}\033[0m\n"

def test_blue_full_text_color(capfd: object) -> None:
    text = "This is BLUE!"
    blue(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[34m{text}\033[0m\n"

def test_cyan_full_text_color(capfd: object) -> None:
    text = "This is CYAN!"
    cyan(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[36m{text}\033[0m\n"

def test_white_full_text_color(capfd: object) -> None:
    text = "This is WHITE!"
    white(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[37m{text}\033[0m\n"

def test_black_full_text_color(capfd: object) -> None:
    text = "This is BLACK!"
    black(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[30m{text}\033[0m\n"
