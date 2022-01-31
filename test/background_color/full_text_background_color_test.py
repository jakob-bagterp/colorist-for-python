from colorist import bg_green, bg_yellow, bg_red, bg_magenta, bg_blue, bg_cyan, bg_white, bg_black
import terminal

class TestFullTextBackgroundColor():
    def test_green_full_text_color(self, capfd: object) -> None:
        text = "This is GREEN background!"
        bg_green(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[42m{text}\033[0m\n"

    def test_yellow_full_text_color(self, capfd: object) -> None:
        text = "This is YELLOW background!"
        bg_yellow(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[43m{text}\033[0m\n"

    def test_red_full_text_color(self, capfd: object) -> None:
        text = "This is RED background!"
        bg_red(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[41m{text}\033[0m\n"

    def test_magenta_full_text_color(self, capfd: object) -> None:
        text = "This is MAGENTA background!"
        bg_magenta(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[45m{text}\033[0m\n"

    def test_blue_full_text_color(self, capfd: object) -> None:
        text = "This is BLUE background!"
        bg_blue(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[44m{text}\033[0m\n"

    def test_cyan_full_text_color(self, capfd: object) -> None:
        text = "This is CYAN background!"
        bg_cyan(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[46m{text}\033[0m\n"

    def test_white_full_text_color(self, capfd: object) -> None:
        text = "This is WHITE background!"
        bg_white(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[47m{text}\033[0m\n"

    def test_black_full_text_color(self, capfd: object) -> None:
        text = "This is BLACK background!"
        bg_black(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[40m{text}\033[0m\n"
