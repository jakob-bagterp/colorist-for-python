
import pytest

from colorist import ColorRGB


@pytest.mark.parametrize("rgb, expected_repr", [
    ((0, 0, 0), "R: 0, G: 0, B: 0"),
    ((137, 53, 238), "R: 137, G: 53, B: 238"),
    ((255, 255, 255), "R: 255, G: 255, B: 255"),
])
def test_repr_of_color_rgb(rgb: tuple[int, int, int], expected_repr: str) -> None:
    color_rgb = ColorRGB(*rgb)
    assert repr(color_rgb) == expected_repr
