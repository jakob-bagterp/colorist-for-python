from colorist import bg_bright_green, bg_bright_yellow, bg_bright_red, bg_bright_magenta, bg_bright_blue, bg_bright_cyan, bg_bright_white, bg_bright_black
import terminal

class TestFullTextBackgroundBrightColor():
    def test_bright_green_full_text_color(self, capfd: object) -> None:
        text = "This is GREEN background!"
        bg_bright_green(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[102m{text}\033[0m\n"

    def test_bright_yellow_full_text_color(self, capfd: object) -> None:
        text = "This is YELLOW background!"
        bg_bright_yellow(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[103m{text}\033[0m\n"

    def test_bright_red_full_text_color(self, capfd: object) -> None:
        text = "This is RED background!"
        bg_bright_red(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[101m{text}\033[0m\n"

    def test_bright_magenta_full_text_color(self, capfd: object) -> None:
        text = "This is MAGENTA background!"
        bg_bright_magenta(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[105m{text}\033[0m\n"

    def test_bright_blue_full_text_color(self, capfd: object) -> None:
        text = "This is BLUE background!"
        bg_bright_blue(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[104m{text}\033[0m\n"

    def test_bright_cyan_full_text_color(self, capfd: object) -> None:
        text = "This is CYAN background!"
        bg_bright_cyan(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[106m{text}\033[0m\n"

    def test_bright_white_full_text_color(self, capfd: object) -> None:
        text = "This is WHITE background!"
        bg_bright_white(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[107m{text}\033[0m\n"

    def test_bright_black_full_text_color(self, capfd: object) -> None:
        text = "This is BLACK background!"
        bg_bright_black(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[100m{text}\033[0m\n"
