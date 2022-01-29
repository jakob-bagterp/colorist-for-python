from colorist import bright_green, bright_yellow, bright_red, bright_magenta, bright_blue, bright_cyan, bright_white, bright_black
import terminal

class TestFullTextBrightColor():
    def test_bright_green_full_text_color(self, capfd: object) -> None:
        text = "This is GREEN!"
        bright_green(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[92m{text}\033[0m\n"

    def test_bright_yellow_full_text_color(self, capfd: object) -> None:
        text = "This is YELLOW!"
        bright_yellow(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[93m{text}\033[0m\n"

    def test_bright_red_full_text_color(self, capfd: object) -> None:
        text = "This is RED!"
        bright_red(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[91m{text}\033[0m\n"

    def test_bright_magenta_full_text_color(self, capfd: object) -> None:
        text = "This is MAGENTA!"
        bright_magenta(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[95m{text}\033[0m\n"

    def test_bright_blue_full_text_color(self, capfd: object) -> None:
        text = "This is BLUE!"
        bright_blue(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[94m{text}\033[0m\n"

    def test_bright_cyan_full_text_color(self, capfd: object) -> None:
        text = "This is CYAN!"
        bright_cyan(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[96m{text}\033[0m\n"

    def test_bright_white_full_text_color(self, capfd: object) -> None:
        text = "This is WHITE!"
        bright_white(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[97m{text}\033[0m\n"

    def test_bright_black_full_text_color(self, capfd: object) -> None:
        text = "This is BLACK!"
        bright_black(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[90m{text}\033[0m\n"
