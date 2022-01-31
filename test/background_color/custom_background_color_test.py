from colorist import BgColor
import terminal

class TestCustomBackgroundColor():
    def test_custom_text_background_color_1(self, capfd: object) -> None:
        print(f"I want {BgColor.RED}red{BgColor.OFF} background color inside this paragraph")
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == "I want \033[41mred\033[0m background color inside this paragraph\n"

    def test_custom_text_background_color_2(self, capfd: object) -> None:
        print(f"Both {BgColor.GREEN}green{BgColor.OFF} and {BgColor.YELLOW}yellow{BgColor.OFF} are nice background colors")
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == "Both \033[42mgreen\033[0m and \033[43myellow\033[0m are nice background colors\n"
