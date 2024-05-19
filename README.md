[![Latest version](https://img.shields.io/static/v1?label=version&message=1.7.3&color=yellowgreen)](https://github.com/jakob-bagterp/colorist-for-python/releases/latest)
[![Python 3.10 | 3.11 | 3.12 or higher](https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11%20|%203.12%2B&color=blueviolet)](https://www.python.org)
[![BSD-3-Clause license](https://img.shields.io/static/v1?label=license&message=BSD-3-Clause&color=blue)](https://github.com/jakob-bagterp/colorist-for-python/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/colorist-for-python/branch/master/graph/badge.svg?token=1E69VOP4ED)](https://codecov.io/gh/jakob-bagterp/colorist-for-python)
[![CodeQL](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/codeql.yml/badge.svg)](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/codeql.yml)
[![Test](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/colorist)](https://pepy.tech/project/colorist)

# 🌈 Colorist for Python 🌈
Lightweight Python package that makes it easy and fast to print colored text in the terminal.

Ready to try? See [how to install](https://jakob-bagterp.github.io/colorist-for-python/getting-started/installation/).

## Getting Started
### Print Line of Colored Text
How to print a full line of colored text in the terminal:

```python
from colorist import green, yellow, red

green("This is GREEN!")
yellow("This is YELLOW!")
red("This is RED!")
```

How it appears in the terminal:

![Example of full line of green, yellow, red colored text printed in a terminal window](/docs/assets/images/examples/color_full_text_green_yellow_red.png)

### Print Mixed Text Colors
How to customize colors inside a paragraph and print it in the terminal:

```python
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")

print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
```

How it appears in the terminal:

![Example of white text mixed with green, yellow, red colors printed in a terminal window](/docs/assets/images/examples/color_custom_text_green_yellow_red.png)

## Other Styling Options
### Print Bright Colors
Most terminals support bright colors that stand more out:

```python
from colorist import BrightColor

print(f"I want {BrightColor.CYAN}cyan{BrightColor.OFF} color inside this paragraph")
```

How it appears in the terminal:

![Example of white text mixed with cyan printed in a terminal window](/docs/assets/images/examples/bright_color_custom_text_cyan.png)

Remember to use `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the color may spill over and into other terminal messages.

### Print Background Colors
```python
from colorist import bg_green, bg_yellow, bg_red

bg_green("This is GREEN background!")
bg_yellow("This is YELLOW background!")
bg_red("This is RED background!")
```

How it appears in the terminal:

![Example of white text and colored backgrounds if green, yellow, red printed in a terminal window](/docs/assets/images/examples/bg_color_full_text_green_yellow_red.png)

Background colors can also be mixed inside a paragraph:

```python
from colorist import BgColor

print(f"I want {BgColor.RED}red{BgColor.OFF} background color inside this paragraph")

print(f"Both {BgColor.GREEN}green{BgColor.OFF} and {BgColor.YELLOW}yellow{BgColor.OFF} are nice background colors")
```

How it appears in the terminal:

![Example of black, green, yellow, red background colors mixed inside paragraph printed in a terminal window](/docs/assets/images/examples/bg_color_custom_text_green_yellow_red.png)

```python
from colorist import BgBrightColor

print(f"I want {BgBrightColor.CYAN}cyan{BgBrightColor.OFF} background color inside this paragraph")
```

How it appears in the terminal:

![Example of white text on a cyan background color printed in a terminal window](/docs/assets/images/examples/bg_bright_color_custom_text_cyan.png)

As with text colors, remember to use `BgColor.OFF` or `BgBrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the color may spill over and into other terminal messages.

## Foreground Text
| Color | Full Text Function | Custom | Example |
| ----- | ------------------ | ------ | ------- |
| ![Green](/docs/assets/images/colors/green_16x16.png) | `green("text")` | `Color.GREEN` | ![Green text color in terminal](/docs/assets/images/examples/color_map/green_full_text_167x16.png) |
| ![Yellow](/docs/assets/images/colors/yellow_16x16.png) | `yellow("text")` | `Color.YELLOW` | ![Yellow text color in terminal](/docs/assets/images/examples/color_map/yellow_full_text_167x16.png) |
| ![Red](/docs/assets/images/colors/red_16x16.png) | `red("text")` | `Color.RED` | ![Red text color in terminal](/docs/assets/images/examples/color_map/red_full_text_167x16.png) |
| ![Magenta](/docs/assets/images/colors/magenta_16x16.png) | `magenta("text")` | `Color.MAGENTA` | ![Magenta text color in terminal](/docs/assets/images/examples/color_map/magenta_full_text_167x16.png) |
| ![Blue](/docs/assets/images/colors/blue_16x16.png) | `blue("text")` | `Color.BLUE` | ![Blue text color in terminal](/docs/assets/images/examples/color_map/blue_full_text_167x16.png) |
| ![Cyan](/docs/assets/images/colors/cyan_16x16.png) | `cyan("text")` | `Color.CYAN` | ![Cyan text color in terminal](/docs/assets/images/examples/color_map/cyan_full_text_167x16.png) |
| ![White](/docs/assets/images/colors/white_16x16.png) | `white("text")` | `Color.WHITE` | ![White text color in terminal](/docs/assets/images/examples/color_map/white_full_text_167x16.png) |
| ![Black](/docs/assets/images/colors/black_16x16.png) | `black("text")` | `Color.BLACK` | ![Black text color in terminal](/docs/assets/images/examples/color_map/black_full_text_167x16.png) |
| - | - | `Color.DEFAULT` | - |
| - | - | `Color.OFF` | - |
| ![Bright green](/docs/assets/images/colors/bright_green_16x16.png) | `bright_green("text")` | `BrightColor.GREEN` | ![Bright green text color in terminal](/docs/assets/images/examples/color_map/bright_green_full_text_167x16.png) |
| ![Bright yellow](/docs/assets/images/colors/bright_yellow_16x16.png) | `bright_yellow("text")` | `BrightColor.YELLOW` | ![Bright yellow text color in terminal](/docs/assets/images/examples/color_map/bright_yellow_full_text_167x16.png) |
| ![Bright red](/docs/assets/images/colors/bright_red_16x16.png) | `bright_red("text")` | `BrightColor.RED` | ![Bright red text color in terminal](/docs/assets/images/examples/color_map/bright_red_full_text_167x16.png) |
| ![Bright magenta](/docs/assets/images/colors/bright_magenta_16x16.png) | `bright_magenta("text")` | `BrightColor.MAGENTA` | ![Bright magenta text color in terminal](/docs/assets/images/examples/color_map/bright_magenta_full_text_167x16.png) |
| ![Bright blue](/docs/assets/images/colors/bright_blue_16x16.png) | `bright_blue("text")` | `BrightColor.BLUE` | ![Bright blue text color in terminal](/docs/assets/images/examples/color_map/bright_blue_full_text_167x16.png) |
| ![Bright cyan](/docs/assets/images/colors/bright_cyan_16x16.png) | `bright_cyan("text")` | `BrightColor.CYAN` | ![Bright cyan text color in terminal](/docs/assets/images/examples/color_map/bright_cyan_full_text_167x16.png) |
| ![Bright white](/docs/assets/images/colors/bright_white_16x16.png) | `bright_white("text")` | `BrightColor.WHITE` | ![Bright white text color in terminal](/docs/assets/images/examples/color_map/bright_white_full_text_167x16.png) |
| ![Bright black](/docs/assets/images/colors/bright_black_16x16.png) | `bright_black("text")` | `BrightColor.BLACK` | ![Bright black text color in terminal](/docs/assets/images/examples/color_map/bright_black_full_text_167x16.png) |
| - | - | `BrightColor.DEFAULT` | - |
| - | - | `BrightColor.OFF` | - |

## Background
| Color | Full Text Function | Custom | Example |
| ----- | ------------------ | ------ | ------- |
| ![Green](/docs/assets/images/colors/green_16x16.png) | `bg_green("text")` | `BgColor.GREEN` | ![Green background color in terminal](/docs/assets/images/examples/bg_color_map/green_full_text_194x16.png) |
| ![Yellow](/docs/assets/images/colors/yellow_16x16.png) | `bg_yellow("text")` | `BgColor.YELLOW` | ![Yellow background color in terminal](/docs/assets/images/examples/bg_color_map/yellow_full_text_194x16.png) |
| ![Red](/docs/assets/images/colors/red_16x16.png) | `bg_red("text")` | `BgColor.RED` | ![Red background color in terminal](/docs/assets/images/examples/bg_color_map/red_full_text_194x16.png) |
| ![Magenta](/docs/assets/images/colors/magenta_16x16.png) | `bg_magenta("text")` | `BgColor.MAGENTA` | ![Magenta background color in terminal](/docs/assets/images/examples/bg_color_map/magenta_full_text_194x16.png) |
| ![Blue](/docs/assets/images/colors/blue_16x16.png) | `bg_blue("text")` | `BgColor.BLUE` | ![Blue background color in terminal](/docs/assets/images/examples/bg_color_map/blue_full_text_194x16.png) |
| ![Cyan](/docs/assets/images/colors/cyan_16x16.png) | `bg_cyan("text")` | `BgColor.CYAN` | ![Cyan background color in terminal](/docs/assets/images/examples/bg_color_map/cyan_full_text_194x16.png) |
| ![White](/docs/assets/images/colors/white_16x16.png) | `bg_white("text")` | `BgColor.WHITE` | ![White background color in terminal](/docs/assets/images/examples/bg_color_map/white_full_text_194x16.png) |
| ![Black](/docs/assets/images/colors/black_16x16.png) | `bg_black("text")` | `BgColor.BLACK` | ![Black background color in terminal](/docs/assets/images/examples/bg_color_map/black_full_text_194x16.png) |
| - | - | `BgColor.DEFAULT` | - |
| - | - | `BgColor.OFF` | - |
| ![Bright green](/docs/assets/images/colors/bright_green_16x16.png) | `bg_bright_green("text")` | `BgBrightColor.GREEN` | ![Bright green background color in terminal](/docs/assets/images/examples/bg_color_map/bright_green_full_text_194x16.png) |
| ![Bright yellow](/docs/assets/images/colors/bright_yellow_16x16.png) | `bg_bright_yellow("text")` | `BgBrightColor.YELLOW` | ![Bright yellow background color in terminal](/docs/assets/images/examples/bg_color_map/bright_yellow_full_text_194x16.png) |
| ![Bright red](/docs/assets/images/colors/bright_red_16x16.png) | `bg_bright_red("text")` | `BgBrightColor.RED` | ![Bright red background color in terminal](/docs/assets/images/examples/bg_color_map/bright_red_full_text_194x16.png) |
| ![Bright magenta](/docs/assets/images/colors/bright_magenta_16x16.png) | `bg_bright_magenta("text")` | `BgBrightColor.MAGENTA` | ![Bright magenta background color in terminal](/docs/assets/images/examples/bg_color_map/bright_magenta_full_text_194x16.png) |
| ![Bright blue](/docs/assets/images/colors/bright_blue_16x16.png) | `bg_bright_blue("text")` | `BgBrightColor.BLUE` | ![Bright blue background color in terminal](/docs/assets/images/examples/bg_color_map/bright_blue_full_text_194x16.png) |
| ![Bright cyan](/docs/assets/images/colors/bright_cyan_16x16.png) | `bg_bright_cyan("text")` | `BgBrightColor.CYAN` | ![Bright cyan background color in terminal](/docs/assets/images/examples/bg_color_map/bright_cyan_full_text_194x16.png) |
| ![Bright white](/docs/assets/images/colors/bright_white_16x16.png) | `bg_bright_white("text")` | `BgBrightColor.WHITE` | ![Bright white background color in terminal](/docs/assets/images/examples/bg_color_map/bright_white_full_text_194x16.png) |
| ![Bright black](/docs/assets/images/colors/bright_black_16x16.png) | `bg_bright_black("text")` | `BgBrightColor.BLACK` | ![Bright black background color in terminal](/docs/assets/images/examples/bg_color_map/bright_black_full_text_194x16.png) |
| - | - | `BgBrightColor.DEFAULT` | - |
| - | - | `BgBrightColor.OFF` | - |

# Thank You for Supporting
## Donate
This module is free to use. And if you like it, feel free to [buy me a coffee](https://github.com/sponsors/jakob-bagterp).

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/colorist-for-python/pulls).

## Report Bugs
Report bugs and issues [here](https://github.com/jakob-bagterp/colorist-for-python/issues).
