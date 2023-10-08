---
tags:
    - Documentation
    - Tutorial
---

# ANSI Escape Codes
Colorist uses ANSI escape codes to style text in the terminal. This page explains how ANSI escape codes work, and how to use them in your own code.

## What Are ANSI Escape Codes?
ANSI escape sequences were introduced in the 1970s as a standard to style text terminals with color, font styling, and other options. They are supported by most modern terminals in operating systems like Windows, macOS, and Linux.

They always start with `\x1b`, `\e`, or `\033` depending on the operating system or programming language. Technically this inserts byte 27 into a string, which is equivalent to `0x1b` and the `ESC` key when you look at an [ASCII table](https://www.asciitable.com). Hence the name.

Though ANSI escape sequences appear in a string as multiple characters, they are in reality interpreted by the terminal as a single command. For example:

* `\x1b[31m`: Change the color to red
* `\x1b[0m`: Reset any styling

How to apply this in a print command:

```python
print(f"I want \x1b[31mred\x1b[0m color inside this paragraph")
```

And yet, the characters of the sequences are hidden in the terminal output apart from the color change:

<pre><code>% I want <span class="fg-red">red</span> color inside this paragraph</code></pre>

## Humanised Sequences
This is also why it's [convenient to use Colorist](../standard-colors/text-foreground.md) instead of manually writing raw ANSI escape codes. The `Color` class will generate the ANSI escape sequences and keep the code readable. This example generates the same terminal output as above:

```python
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")
```

## Standard Colors
### Color Codes and Building Blocks
All ANSI escape sequences follow the same pattern. For example, the sequence `\x1b[31m` can be broken down into:

* `\x1b[`: Starts sequence, also called the Control Sequence Introducer (CSI)
* `31`: The color code
* `m`: Ends sequence, also called the Select Graphic Rendition (SGR)

There are 8 standard colors and 8 bright colors – 16 in total. The bright colors are the same as the standard colors, yet with a higher intensity, and each color can be in the foreground (i.e. as text) or background.

The 8 colors are simply black and white, plus the 6 colors of the rainbow. Firstly, the three primary colors red, green, and blue. Then the secondary colors yellow, magenta, and cyan:

| Code | Color   | Example |
| :--: | :-----: | :-----: |
| 0    | Black   | ![Black](../../assets/images/colors/black_16x16.png) |
| 1    | Red     | ![Red](../../assets/images/colors/red_16x16.png) |
| 2    | Green   | ![Green](../../assets/images/colors/green_16x16.png) |
| 3    | Yellow  | ![Yellow](../../assets/images/colors/yellow_16x16.png) |
| 4    | Blue    | ![Blue](../../assets/images/colors/blue_16x16.png) |
| 5    | Magenta | ![Magenta](../../assets/images/colors/magenta_16x16.png) |
| 6    | Cyan    | ![Cyan](../../assets/images/colors/cyan_16x16.png) |
| 7    | White   | ![White](../../assets/images/colors/white_16x16.png) |

Each color then needs to be prepended by a foreground or background option. When combining the two codes – simply replace the underscore `_` with the missing color code – `34` for example is blue text, and `44` is blue background:

| Code | Placement  | Intensity |
| :--: | :--------: | :-------: |
| 3_   | Text       | Standard  |
| 4_   | Background | Standard  |
| 9_   | Text       | Bright    |
| 10_  | Background | Bright    |

### Foreground Text and Background Colors
To apply different color and styling options, simply replace the two underscores `__` in `\x1b[__m` with any of the following color codes:

| Color   | Example | Text | Background | Bright Example | Bright Text | Bright Background |
| :-----: | :-----: | :--: | :--------: | :------------: | :---------: | :---------------: |
| Black   | ![Black](../../assets/images/colors/black_16x16.png) | 30 | 40 | ![Bright black](../../assets/images/colors/bright_black_16x16.png) | 90 | 100 |
| Red     | ![Red](../../assets/images/colors/red_16x16.png) | 31 | 41 | ![Bright red](../../assets/images/colors/bright_red_16x16.png) | 91 | 101 |
| Green   | ![Green](../../assets/images/colors/green_16x16.png) | 32 | 42 | ![Bright green](../../assets/images/colors/bright_green_16x16.png) | 92 | 102 |
| Yellow  | ![Yellow](../../assets/images/colors/yellow_16x16.png) | 33 | 43 | ![Bright yellow](../../assets/images/colors/bright_yellow_16x16.png) | 93 | 103 |
| Blue    | ![Blue](../../assets/images/colors/blue_16x16.png) | 34 | 44 | ![Bright blue](../../assets/images/colors/bright_blue_16x16.png) | 94 | 104 |
| Magenta | ![Magenta](../../assets/images/colors/magenta_16x16.png) | 35 | 45 | ![Bright magenta](../../assets/images/colors/bright_magenta_16x16.png) | 95 | 105 |
| Cyan    | ![Cyan](../../assets/images/colors/cyan_16x16.png) | 36 | 46 | ![Bright cyan](../../assets/images/colors/bright_cyan_16x16.png) | 96 | 106 |
| White   | ![White](../../assets/images/colors/white_16x16.png) | 37 | 47 | ![Bright white](../../assets/images/colors/bright_white_16x16.png) | 97 | 107 |
| Default | | 39 | 49 | |  99 | 109 |
| Reset   | | 0 | 0 | | 0 | 0 |

!!! tip
    Remember to use `\x1b[0m` every time you want to revert back to the default terminal text style. Otherwise, any color or styling may spill over and into other terminal messages.

    When using Colorist, you can for example use `Color.OFF` to reset the terminal text style.

### Effects
For effects, the codes are. And as before, replace the two underscores `__` in `\x1b[__m` with any of the following color codes:

| Effect    | On  | Off | Example |
| :-------: | :-: | :-: | :-----: |
| Bold      | 1   | 21  | <code>This is <strong>BOLD</strong></code> |
| Dim       | 2   | 22  | <code><span class="effect-dimmed">This is DIMMED</span></code> |
| Underline | 4   | 24  | <code>This is <u>UNDERLINED</u></code> |
| Blink     | 5   | 25  | <code><span class="effect-blinking">This is BLINKING</span></code> |
| Reverse   | 7   | 27  | ![Reverse](../../assets/images/examples/effect_map/reverse_full_text_140x16.png) |
| Hide      | 8   | 28  | ![Hide](../../assets/images/examples/effect_map/hide_full_text_140x16.png) |

!!! info "Different Color Schemes in Different Terminals"
    Most terminals apply different color schemes so `\x1b[31m` or `Color.RED` won't produce the exact same screen color of red. Some straight, others with an orange tint. For further reading, refer to this [list of common terminals and their color schemes](https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit).

## Non-Standard Colors
To have more control of the colors or want to be more creative, you aren't limited to 16 colors. In addition, the escape codes can be used with an extended 256 color palette or the [RGB color space](../extended-colors/rgb.md).

!!! info "Not All Terminals Support Extended Color Palettes"
    While most terminals support the standard ANSI color sequences, far from all support the extended 256 or RGB color space. For example, the Windows Command Prompt does not support RGB colors while the Windows Terminal does support RGB colors.

    Refer to the terminal's documentation to see if it supports extended color palettes.

### Extended 256 Colors
The [extended palette of 256 colors](https://commons.wikimedia.org/wiki/File:Xterm_256color_chart.svg) is a 6x6x6 color cube, with 216 colors, plus 24 shades of gray. The color cube is made up of 6 levels of red, green, and blue, respectively. The color cube is then combined with the 24 shades of gray to make up the 256 colors.

It works both with foreground text and background colors. Simply replace the two underscores `__` with any number from `0` to `255`:

| Code            | Placement  |
| :-------------: | :--------: |
| `\x1b[38;5;__m` | Text       |
| `\x1b[48;5;__m` | Background |

For example, `\x1b[38;5;243m` is a light gray foreground text color, and `\x1b[48;5;243m` is a light gray background color.

### RGB Colors
The RGB color space represents a much broader array of colors. Simply use any number from `0` to `255` to set each of the red `r`, green `g`, and blue `b` colors in the sequences `38;2;r;g;b` for text color and `38;2;r;g;b` for background color:

| Code               | Placement  |
| :----------------: | :--------: |
| `\x1b[38;2;r;g;bm` | Text       |
| `\x1b[48;2;r;g;bm` | Background |

For example, `\x1b[38;2;255;0;0m` is a red foreground text color, and `\x1b[48;2;255;0;0m` is a red background color.

In Colorist, the [RGB color space](../extended-colors/rgb.md) is used to furthermore support definition of colors as [HSL](../extended-colors/hsl.md) or [Hex](../extended-colors/hex.md).
