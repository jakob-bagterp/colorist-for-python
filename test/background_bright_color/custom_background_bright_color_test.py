from colorist import BgBrightColor
import terminal

def test_custom_text_background_color_1(capfd: object) -> None:
    print(f"I want {BgBrightColor.CYAN}cyan{BgBrightColor.OFF} background color inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == "I want \033[106mcyan\033[0m background color inside this paragraph\n"
