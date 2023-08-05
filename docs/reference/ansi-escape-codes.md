---
tags:
    - Documentation
    - Tutorial
---

# ANSI Escape Codes
## What Are ANSI Escape Codes?
ANSI escape sequences were introduced in the 1970s as a standard to style text terminals with color, font styling, and other options. They are supported by most modern terminals in operating systems like Windows, macOS, and Linux.

They always start with `\x1b`, or `\e`, or `\033` depending on the operating system. Technically this inserts byte 27 into a string, which is equivalent to `0x1b` and the `ESC` key when you look at an [ASCII table](https://www.asciitable.com). Hence the name.

Though ANSI escape sequences appear in a string as multiple characters, they are in reality interpreted by the terminal as a single command. For example:

* `\x1b[31m`: Change the color to red
* `\x1b[0m`: Reset any styling

How to apply this in a print command:

```python
print(f"I want \x1b[31mred\x1b[0m color inside this paragraph")
```

And yet, the characters of the sequences are hidden in the terminal output:

![Example of terminal message with red text color](../assets/images/examples/color_custom_text_red.png)

## Humanised Sequences
This is also why it's convenient to use Colorist instead of manually writing raw ANSI escape codes. The `Color` class will generate the ANSI escape sequences and keep the code readable. This example generates the same terminal output as above:

```python
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")
```

## Overview of Standard Colors
All ANSI escape sequences follow the same pattern. The sequence `\x1b[31m` can be broken down into:

* `\x1b[`: Starts sequence, also called the Control Sequence Introducer (CSI)
* `31`: The color code
* `m`: Ends sequence, also called the Select Graphic Rendition (SGR)

There are 8 standard colors and 8 bright colors – 16 in total. The bright colors are the same as the standard colors, yet with a higher intensity, and each color can be in the foreground (i.e. as text) or background.

| Code | Color   |
| :--: | :-----: |
| 0    | Black   |
| 1    | Red     |
| 2    | Green   |
| 3    | Yellow  |
| 4    | Blue    |
| 5    | Magenta |
| 6    | Cyan    |
| 7    | White   |

Each color needs to be prepended with a foreground and background option. The foreground option is the default, and the background option is the same color code plus 10. When combining the two codes, `34` for example is blue text, and `44` is blue background:

| Code | Placement  | Intensity |
| :--: | :--------: | :-------: |
| 3x   | Foreground | Standard  |
| 4x   | Background | Standard  |
| 9x   | Foreground | Bright    |
| 10x  | Background | Bright    |

### Foreground Text and Background Colors
To apply different color and styling options, simply replace the two underscores `__` in `\x1b[__m` with any of the following color codes:

| Color   | Example | Text | Background | Bright Text | Bright Background |
| :-----: | :-----: | :--: | :--------: | :---------: | :---------------: |
| Black   | ![Black](../assets/images/colors/black_16x16.png) | 30 | 40 | 90 | 100 |
| Red     | ![Red](../assets/images/colors/red_16x16.png) | 31 | 41 | 91 | 101 |
| Green   | ![Green](../assets/images/colors/green_16x16.png) | 32 | 42 | 92 | 102 |
| Yellow  | ![Yellow](../assets/images/colors/yellow_16x16.png) | 33 | 43 | 93 | 103 |
| Blue    | ![Blue](../assets/images/colors/blue_16x16.png) | 34 | 44 | 94 | 104 |
| Magenta | ![Magenta](../assets/images/colors/magenta_16x16.png) | 35 | 45 | 95 | 105 |
| Cyan    | ![Cyan](../assets/images/colors/cyan_16x16.png) | 36 | 46 | 96 | 106 |
| White   | ![White](../assets/images/colors/white_16x16.png) | 37 | 47 | 97 | 107 |
| Default | | 39 | 49 | 99 | 109 |
| Reset   | | 0 | 0 | 0 | 0 |

!!! tip
    Remember to use `\033[0m` every time you want to revert back to the default terminal text style. Otherwise, any color or styling may spill over and into other terminal messages.

### Effects
For effects, the codes are:

| Effect    | On  | Off | Example |
| :-------: | :-: | :-: | :-----: |
| Bold      | 1   | 21  | ![Bold](../assets/images/examples/effect_map/bold_full_text_140x16.png) |
| Dim       | 2   | 22  | ![Dim](../assets/images/examples/effect_map/dim_full_text_140x16.png) |
| Underline | 4   | 24  | ![Underline](../assets/images/examples/effect_map/underline_full_text_140x16.png) |
| Blink     | 5   | 25  | ![Blink](../assets/images/examples/effect_map/blink_full_text_140x16.gif) |
| Reverse   | 7   | 27  | ![Reverse](../assets/images/examples/effect_map/reverse_full_text_140x16.png) |
| Hide      | 8   | 28  | ![Hide](../assets/images/examples/effect_map/hide_full_text_140x16.png) |

!!! info "Different Color Schemes in Different Terminals"
    Most terminals apply different color schemes so `\x1b[31m` or `Color.RED` won't produce the exact same screen color of red. Some straight, others with an orange tint. For further reading, refer to this [list of common terminals and their color schemes](https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit).
