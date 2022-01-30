from colorist import BrightColor
import terminal

class TestCustomBrightColor():
    def test_custom_text_color_1(self, capfd: object) -> None:
        print(f"I want {BrightColor.CYAN}cyan{BrightColor.RESET} color inside this paragraph")
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == "I want \033[96mcyan\033[0m color inside this paragraph\n"
