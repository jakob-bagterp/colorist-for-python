
import pytest

from colorist import ColorHSL


@pytest.mark.parametrize("hsl, expected_repr", [
    ((0, 0, 0), "H: 0, S: 0, L: 0"),
    ((137, 24, 82), "H: 137, S: 24, L: 82"),
    ((360, 100, 100), "H: 360, S: 100, L: 100"),
])
def test_repr_of_color_hsl(hsl: tuple[int, int, int], expected_repr: str) -> None:
    color_hsl = ColorHSL(*hsl)
    assert repr(color_hsl) == expected_repr
