---
title: How to Use Colors in ANSI Escape Codes
description: Learn how to print colored text in terminal output using Python and ANSI escape codes. Includes color maps and code examples.
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
    - Standard Colors
    - Background Colors
    - Text Colors
    - Foreground Colors
---

# Standard 16 Colors in ANSI Escape Codes
## Structure
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
| Black   | ![Black](../assets/images/colors/black_16x16.png)     | 30 | 40 | ![Bright black](../assets/images/colors/bright_black_16x16.png)     | 90 | 100 |
| Red     | ![Red](../assets/images/colors/red_16x16.png)         | 31 | 41 | ![Bright red](../assets/images/colors/bright_red_16x16.png)         | 91 | 101 |
| Green   | ![Green](../assets/images/colors/green_16x16.png)     | 32 | 42 | ![Bright green](../assets/images/colors/bright_green_16x16.png)     | 92 | 102 |
| Yellow  | ![Yellow](../assets/images/colors/yellow_16x16.png)   | 33 | 43 | ![Bright yellow](../assets/images/colors/bright_yellow_16x16.png)   | 93 | 103 |
| Blue    | ![Blue](../assets/images/colors/blue_16x16.png)       | 34 | 44 | ![Bright blue](../assets/images/colors/bright_blue_16x16.png)       | 94 | 104 |
| Magenta | ![Magenta](../assets/images/colors/magenta_16x16.png) | 35 | 45 | ![Bright magenta](../assets/images/colors/bright_magenta_16x16.png) | 95 | 105 |
| Cyan    | ![Cyan](../assets/images/colors/cyan_16x16.png)       | 36 | 46 | ![Bright cyan](../assets/images/colors/bright_cyan_16x16.png)       | 96 | 106 |
| White   | ![White](../assets/images/colors/white_16x16.png)     | 37 | 47 | ![Bright white](../assets/images/colors/bright_white_16x16.png)     | 97 | 107 |
| Default | | 39 | 49 | |  99 | 109 |
| Reset   | | 0 | 0 | | 0 | 0 |

!!! tip
    Remember to use `\x1b[0m` every time you want to revert back to the default terminal text style. Otherwise, any color or styling may spill over and into other terminal messages.

    When using Colorist, you can for example use `Color.OFF` to reset the terminal text style.

### Examples
How to apply the escape color codes:

```python linenums="1"
print("This is \x1b[31mRED\x1b[0m text")
print("This is \x1b[41mRED\x1b[0m background")
print("This is \x1b[91mBRIGHT RED\x1b[0m text")
print("This is \x1b[101mBRIGHT RED\x1b[0m background")
```

How it appears in the terminal:

<pre><code>% This is <span class="fg-red">RED</span> text
% This is <span class="bg-red">RED</span> background
% This is <span class="fg-bright-red">BRIGHT RED</span> text
% This is <span class="bg-bright-red">BRIGHT RED</span> background</code></pre>

## Cheat Sheets
### Foreground Text Colors
#### Standard Colors
| Example | Color | Code | Escape Code | Output Example |
| :-----: | :---: | :--: | :---------: | :------------- |
| ![Black](../assets/images/colors/black_16x16.png)     | Black   | 30 | `\x1b[30m` | <code>This is <span class="fg-black">BLACK</span></code> |
| ![Red](../assets/images/colors/red_16x16.png)         | Red     | 31 | `\x1b[31m` | <code>This is <span class="fg-red">RED</span></code> |
| ![Green](../assets/images/colors/green_16x16.png)     | Green   | 32 | `\x1b[32m` | <code>This is <span class="fg-green">GREEN</span></code> |
| ![Yellow](../assets/images/colors/yellow_16x16.png)   | Yellow  | 33 | `\x1b[33m` | <code>This is <span class="fg-yellow">YELLOW</span></code> |
| ![Blue](../assets/images/colors/blue_16x16.png)       | Blue    | 34 | `\x1b[34m` | <code>This is <span class="fg-blue">BLUE</span></code> |
| ![Magenta](../assets/images/colors/magenta_16x16.png) | Magenta | 35 | `\x1b[35m` | <code>This is <span class="fg-magenta">MAGENTA</span></code> |
| ![Cyan](../assets/images/colors/cyan_16x16.png)       | Cyan    | 36 | `\x1b[36m` | <code>This is <span class="fg-cyan">CYAN</span></code> |
| ![White](../assets/images/colors/white_16x16.png)     | White   | 37 | `\x1b[37m` | <code>This is <span class="fg-white">WHITE</span></code> |

#### Bright Colors
| Example | Color   | Code | Escape Code | Output Example |
| :-----: | :-----: | :--: | :---------: | :------------- |
| ![Bright black](../assets/images/colors/bright_black_16x16.png)     | Black   | 90 | `\x1b[90m` | <code>This is <span class="fg-bright-black">BRIGHT BLACK</span></code> |
| ![Bright red](../assets/images/colors/bright_red_16x16.png)         | Red     | 91 | `\x1b[91m` | <code>This is <span class="fg-bright-red">BRIGHT RED</span></code> |
| ![Bright green](../assets/images/colors/bright_green_16x16.png)     | Green   | 92 | `\x1b[92m` | <code>This is <span class="fg-bright-green">BRIGHT GREEN</span></code> |
| ![Bright yellow](../assets/images/colors/bright_yellow_16x16.png)   | Yellow  | 93 | `\x1b[93m` | <code>This is <span class="fg-bright-yellow">BRIGHT YELLOW</span></code> |
| ![Bright blue](../assets/images/colors/bright_blue_16x16.png)       | Blue    | 94 | `\x1b[94m` | <code>This is <span class="fg-bright-blue">BRIGHT BLUE</span></code> |
| ![Bright magenta](../assets/images/colors/bright_magenta_16x16.png) | Magenta | 95 | `\x1b[95m` | <code>This is <span class="fg-bright-magenta">BRIGHT MAGENTA</span></code> |
| ![Bright cyan](../assets/images/colors/bright_cyan_16x16.png)       | Cyan    | 96 | `\x1b[96m` | <code>This is <span class="fg-bright-cyan">BRIGHT CYAN</span></code> |
| ![Bright white](../assets/images/colors/bright_white_16x16.png)     | White   | 97 | `\x1b[97m` | <code>This is <span class="fg-bright-white">BRIGHT WHITE</span></code> |

### Background Colors
#### Standard Colors
| Example | Color   | Code | Escape Code | Output Example |
| :-----: | :-----: | :--: | :---------: | :------------- |
| ![Black](../assets/images/colors/black_16x16.png)     | Black   | 40 | `\x1b[40m` | <code>This is <span class="bg-black">BLACK</span></code> |
| ![Red](../assets/images/colors/red_16x16.png)         | Red     | 41 | `\x1b[41m` | <code>This is <span class="bg-red">RED</span></code> |
| ![Green](../assets/images/colors/green_16x16.png)     | Green   | 42 | `\x1b[42m` | <code>This is <span class="bg-green">GREEN</span></code> |
| ![Yellow](../assets/images/colors/yellow_16x16.png)   | Yellow  | 43 | `\x1b[43m` | <code>This is <span class="bg-yellow">YELLOW</span></code> |
| ![Blue](../assets/images/colors/blue_16x16.png)       | Blue    | 44 | `\x1b[44m` | <code>This is <span class="bg-blue">BLUE</span></code> |
| ![Magenta](../assets/images/colors/magenta_16x16.png) | Magenta | 45 | `\x1b[45m` | <code>This is <span class="bg-magenta">MAGENTA</span></code> |
| ![Cyan](../assets/images/colors/cyan_16x16.png)       | Cyan    | 46 | `\x1b[46m` | <code>This is <span class="bg-cyan">CYAN</span></code> |
| ![White](../assets/images/colors/white_16x16.png)     | White   | 47 | `\x1b[47m` | <code>This is <span class="bg-white">WHITE</span></code> |

#### Bright Colors
| Example | Color   | Code | Escape Code | Output Example |
| :-----: | :-----: | :--: | :---------: | :------------- |
| ![Bright black](../assets/images/colors/bright_black_16x16.png)     | Black   | 100 | `\x1b[100m` | <code>This is <span class="bg-bright-black">BRIGHT BLACK</span></code> |
| ![Bright red](../assets/images/colors/bright_red_16x16.png)         | Red     | 101 | `\x1b[101m` | <code>This is <span class="bg-bright-red">BRIGHT RED</span></code> |
| ![Bright green](../assets/images/colors/bright_green_16x16.png)     | Green   | 102 | `\x1b[102m` | <code>This is <span class="bg-bright-green">BRIGHT GREEN</span></code> |
| ![Bright yellow](../assets/images/colors/bright_yellow_16x16.png)   | Yellow  | 103 | `\x1b[103m` | <code>This is <span class="bg-bright-yellow">BRIGHT YELLOW</span></code> |
| ![Bright blue](../assets/images/colors/bright_blue_16x16.png)       | Blue    | 104 | `\x1b[104m` | <code>This is <span class="bg-bright-blue">BRIGHT BLUE</span></code> |
| ![Bright magenta](../assets/images/colors/bright_magenta_16x16.png) | Magenta | 105 | `\x1b[105m` | <code>This is <span class="bg-bright-magenta">BRIGHT MAGENTA</span></code> |
| ![Bright cyan](../assets/images/colors/bright_cyan_16x16.png)       | Cyan    | 106 | `\x1b[106m` | <code>This is <span class="bg-bright-cyan">BRIGHT CYAN</span></code> |
| ![Bright white](../assets/images/colors/bright_white_16x16.png)     | White   | 107 | `\x1b[107m` | <code>This is <span class="bg-bright-white">BRIGHT WHITE</span></code> |
