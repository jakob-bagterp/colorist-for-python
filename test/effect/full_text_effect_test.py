from colorist import Color, effect_bold, effect_dim, effect_underline, effect_blink, effect_reverse, effect_hide
import terminal

class TestFullTextEffect():
    def test_bold_full_text_effect(self, capfd: object) -> None:
        text = "This is BOLD!"
        effect_bold(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[39m\033[1m{text}\033[0m\n"

    def test_dim_full_text_effect(self, capfd: object) -> None:
        text = "This is DIMMED!"
        effect_dim(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[39m\033[2m{text}\033[0m\n"

    def test_underline_full_text_effect(self, capfd: object) -> None:
        text = "This is UNDERLINED!"
        effect_underline(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[39m\033[4m{text}\033[0m\n"

    def test_blink_full_text_effect(self, capfd: object) -> None:
        text = "This is BLINKING!"
        effect_blink(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[39m\033[5m{text}\033[0m\n"

    def test_reverse_full_text_effect(self, capfd: object) -> None:
        text = "This is REVERSED!"
        effect_reverse(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[39m\033[7m{text}\033[0m\n"

    def test_hide_full_text_effect(self, capfd: object) -> None:
        text = "This is HIDDEN!"
        effect_hide(text)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[39m\033[8m{text}\033[0m\n"

class TestFullTextEffectWithColor():
    def test_blink_full_text_effect_with_color(self, capfd: object) -> None:
        text = "This is BLINKING!"
        effect_blink(text, Color.CYAN)
        terminal_output = terminal.get_output(capfd)
        assert terminal_output == f"\033[36m\033[5m{text}\033[0m\n"
