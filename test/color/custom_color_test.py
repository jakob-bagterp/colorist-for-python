from colorist import Color
import terminal

_red_text = "I want \033[31mred\033[0m color inside this paragraph\n"

class TestCustomColor():
    def test_custom_text_color_1(self, capfd: object) -> None:
        print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == _red_text

    def test_custom_text_color_2(self, capfd: object) -> None:
        print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == "Both \033[32mgreen\033[0m and \033[33myellow\033[0m are nice colors\n"

    def test_custom_text_color_string_concatenation(self, capfd: object) -> None:
        print("I want {0}red{1} color inside this paragraph".format(Color.RED, Color.OFF))
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == _red_text
