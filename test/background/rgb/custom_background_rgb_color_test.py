import pytest
import terminal

from colorist import BgColorRGB


@pytest.mark.parametrize("rgb, expected", [
    ((255, 255, 255), "Only color this \033[48;2;255;255;255mword\033[0m.\n"),
    ((0, 0, 0), "Only color this \033[48;2;0;0;0mword\033[0m.\n"),
    ((127, 57, 203), "Only color this \033[48;2;127;57;203mword\033[0m.\n"),
])
def test_custom_text_background_rgb_color_f_string(rgb: tuple[int, int, int], expected: str, capfd: object) -> None:
    bg_color_rgb = BgColorRGB(*rgb)
    print(f"Only color this {bg_color_rgb}word{BgColorRGB.OFF}.")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
