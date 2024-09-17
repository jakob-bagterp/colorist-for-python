---
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
    - RGB Colors
---

# RGB Colors in ANSI Escape Codes
The RGB color space represents a much broader array of colors. Simply use any number from `0` to `255` to set each of the red `r`, green `g`, and blue `b` colors in the sequences `38;2;r;g;b` for text color and `38;2;r;g;b` for background color:

| Code               | Placement  |
| :----------------: | :--------: |
| `\x1b[38;2;r;g;bm` | Text       |
| `\x1b[48;2;r;g;bm` | Background |

For example, `\x1b[38;2;255;0;0m` is a red foreground text color, and `\x1b[48;2;255;0;0m` is a red background color.

In Colorist, the [RGB color space](../user-guide/extended-colors/rgb.md) is used to furthermore support definition of colors as [HSL](../user-guide/extended-colors/hsl.md) or [Hex](../user-guide/extended-colors/hex.md).
