---
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
    - Standard Colors
    - Background Colors
    - Text Colors
    - Foreground Colors
---

# Standard Colors in ANSI Escape Codes
## Color Codes
There are 8 standard colors and 8 bright colors – 16 in total. The bright colors are the same as the standard colors, yet with a higher intensity, and each color can be in the foreground (i.e. as text) or background.

The 8 colors are simply black and white, plus the 6 colors of the rainbow. Firstly, the three primary colors red, green, and blue. Then the secondary colors yellow, magenta, and cyan:

| Code | Color   | Example |
| :--: | :-----: | :-----: |
| 0    | Black   | ![Black](../assets/images/colors/black_16x16.png) |
| 1    | Red     | ![Red](../assets/images/colors/red_16x16.png) |
| 2    | Green   | ![Green](../assets/images/colors/green_16x16.png) |
| 3    | Yellow  | ![Yellow](../assets/images/colors/yellow_16x16.png) |
| 4    | Blue    | ![Blue](../assets/images/colors/blue_16x16.png) |
| 5    | Magenta | ![Magenta](../assets/images/colors/magenta_16x16.png) |
| 6    | Cyan    | ![Cyan](../assets/images/colors/cyan_16x16.png) |
| 7    | White   | ![White](../assets/images/colors/white_16x16.png) |

Each color then needs to be prepended by a foreground or background option. When combining the two codes – simply replace the underscore `_` with the missing color code – `34` for example is blue text, and `44` is blue background:

| Code | Placement  | Intensity |
| :--: | :--------: | :-------: |
| 3_   | Text       | Standard  |
| 4_   | Background | Standard  |
| 9_   | Text       | Bright    |
| 10_  | Background | Bright    |

## Foreground Text and Background Colors
To apply different color and styling options, simply replace the two underscores `__` in `\x1b[__m` with any of the following color codes:

| Color   | Example | Text | Background | Bright Example | Bright Text | Bright Background |
| :-----: | :-----: | :--: | :--------: | :------------: | :---------: | :---------------: |
| Black   | ![Black](../assets/images/colors/black_16x16.png) | 30 | 40 | ![Bright black](../assets/images/colors/bright_black_16x16.png) | 90 | 100 |
| Red     | ![Red](../assets/images/colors/red_16x16.png) | 31 | 41 | ![Bright red](../assets/images/colors/bright_red_16x16.png) | 91 | 101 |
| Green   | ![Green](../assets/images/colors/green_16x16.png) | 32 | 42 | ![Bright green](../assets/images/colors/bright_green_16x16.png) | 92 | 102 |
| Yellow  | ![Yellow](../assets/images/colors/yellow_16x16.png) | 33 | 43 | ![Bright yellow](../assets/images/colors/bright_yellow_16x16.png) | 93 | 103 |
| Blue    | ![Blue](../assets/images/colors/blue_16x16.png) | 34 | 44 | ![Bright blue](../assets/images/colors/bright_blue_16x16.png) | 94 | 104 |
| Magenta | ![Magenta](../assets/images/colors/magenta_16x16.png) | 35 | 45 | ![Bright magenta](../assets/images/colors/bright_magenta_16x16.png) | 95 | 105 |
| Cyan    | ![Cyan](../assets/images/colors/cyan_16x16.png) | 36 | 46 | ![Bright cyan](../assets/images/colors/bright_cyan_16x16.png) | 96 | 106 |
| White   | ![White](../assets/images/colors/white_16x16.png) | 37 | 47 | ![Bright white](../assets/images/colors/bright_white_16x16.png) | 97 | 107 |
| Default | | 39 | 49 | |  99 | 109 |
| Reset   | | 0 | 0 | | 0 | 0 |

!!! tip
    Remember to use `\x1b[0m` every time you want to revert back to the default terminal text style. Otherwise, any color or styling may spill over and into other terminal messages.

    When using Colorist, you can for example use `Color.OFF` to reset the terminal text style.
