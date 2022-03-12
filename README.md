[![Latest version](https://img.shields.io/static/v1?label=version&message=1.2.1&color=yellowgreen)](https://github.com/jakob-bagterp/colorist-for-python/releases/latest)
![Python >=3.10](https://img.shields.io/static/v1?label=python&message=>=3.10&color=blueviolet)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://github.com/jakob-bagterp/colorist-for-python/blob/master/LICENSE.md)
[![Test](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/test.yml)

# 🌈 Colorist for Python 🌈
Lightweight Python package that makes it easy and fast to print terminal messages in colors.

## Prerequisites
* Python 3.10 or higher

## Installation
### PyPI
Assuming that Python is installed already, execute this command in the terminal:

```shell
pip3 install colorist
```

If you already have installed Colorist for Python, use this command to upgrade to latest version:

```shell
pip3 install --upgrade colorist
```

### Homebrew
If you already have installed the [Homebrew](https://brew.sh) package manager for Mac and Linux, execute this terminal command to tap Colorist for Python:

```shell
brew tap jakob-bagterp/colorist
```

And then install:

```shell
brew install colorist
```

## Text Colors
### Getting Started
#### Full Terminal Output
How to print a full line of colored text in the terminal:

```python
from colorist import green, yellow, red

green("This is GREEN!")
yellow("This is YELLOW!")
red("This is RED!")
```

How it appears in the terminal:

![Example of terminal message with green, yellow, red text color](/assets/images/examples/color_full_text_green_yellow_red.png)

#### Custom Terminal Output
How to customize terminal messages and change color inside a paragraph:

```python
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")

print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
```

How it appears in the terminal:

![Example of terminal message with green, yellow, red text color](/assets/images/examples/color_custom_text_green_yellow_red.png)


```python
from colorist import BrightColor

print(f"I want {BrightColor.CYAN}cyan{BrightColor.OFF} color inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with cyan text color](/assets/images/examples/bright_color_custom_text_cyan.png)

Remember to use `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise the color may spill over and into other terminal messages.

##### Other String Formats
It's easier and more readable to use f-strings as in the examples above, but you can also use string format:

```python
from colorist import Color

print("I want {0}red{1} color inside this paragraph".format(Color.RED, Color.OFF))
```

How it appears in the terminal:

![Example of terminal message with red text color](/assets/images/examples/color_custom_text_red.png)

### Supported Text Colors
| Color | Full Text Function | Custom | Example |
| ----- | ------------------ | ------ | ------- |
| ![Green](/assets/images/colors/green_16x16.png) | `green("text")` | `Color.GREEN` | ![Green text color in terminal](/assets/images/examples/color_map/green_full_text_167x16.png) |
| ![Yellow](/assets/images/colors/yellow_16x16.png) | `yellow("text")` | `Color.YELLOW` | ![Yellow text color in terminal](/assets/images/examples/color_map/yellow_full_text_167x16.png) |
| ![Red](/assets/images/colors/red_16x16.png) | `red("text")` | `Color.RED` | ![Red text color in terminal](/assets/images/examples/color_map/red_full_text_167x16.png) |
| ![Magenta](/assets/images/colors/magenta_16x16.png) | `magenta("text")` | `Color.MAGENTA` | ![Magenta text color in terminal](/assets/images/examples/color_map/magenta_full_text_167x16.png) |
| ![Blue](/assets/images/colors/blue_16x16.png) | `blue("text")` | `Color.BLUE` | ![Blue text color in terminal](/assets/images/examples/color_map/blue_full_text_167x16.png) |
| ![Cyan](/assets/images/colors/cyan_16x16.png) | `cyan("text")` | `Color.CYAN` | ![Cyan text color in terminal](/assets/images/examples/color_map/cyan_full_text_167x16.png) |
| ![White](/assets/images/colors/white_16x16.png) | `white("text")` | `Color.WHITE` | ![White text color in terminal](/assets/images/examples/color_map/white_full_text_167x16.png) |
| ![Black](/assets/images/colors/black_16x16.png) | `black("text")` | `Color.BLACK` | ![Black text color in terminal](/assets/images/examples/color_map/black_full_text_167x16.png) |
| - | - | `Color.OFF` | - |
| ![Bright green](/assets/images/colors/bright_green_16x16.png) | `bright_green("text")` | `BrightColor.GREEN` | ![Bright green text color in terminal](/assets/images/examples/color_map/bright_green_full_text_167x16.png) |
| ![Bright yellow](/assets/images/colors/bright_yellow_16x16.png) | `bright_yellow("text")` | `BrightColor.YELLOW` | ![Bright yellow text color in terminal](/assets/images/examples/color_map/bright_yellow_full_text_167x16.png) |
| ![Bright red](/assets/images/colors/bright_red_16x16.png) | `bright_red("text")` | `BrightColor.RED` | ![Bright red text color in terminal](/assets/images/examples/color_map/bright_red_full_text_167x16.png) |
| ![Bright magenta](/assets/images/colors/bright_magenta_16x16.png) | `bright_magenta("text")` | `BrightColor.MAGENTA` | ![Bright magenta text color in terminal](/assets/images/examples/color_map/bright_magenta_full_text_167x16.png) |
| ![Bright blue](/assets/images/colors/bright_blue_16x16.png) | `bright_blue("text")` | `BrightColor.BLUE` | ![Bright blue text color in terminal](/assets/images/examples/color_map/bright_blue_full_text_167x16.png) |
| ![Bright cyan](/assets/images/colors/bright_cyan_16x16.png) | `bright_cyan("text")` | `BrightColor.CYAN` | ![Bright cyan text color in terminal](/assets/images/examples/color_map/bright_cyan_full_text_167x16.png) |
| ![Bright white](/assets/images/colors/bright_white_16x16.png) | `bright_white("text")` | `BrightColor.WHITE` | ![Bright white text color in terminal](/assets/images/examples/color_map/bright_white_full_text_167x16.png) |
| ![Bright black](/assets/images/colors/bright_black_16x16.png) | `bright_black("text")` | `BrightColor.BLACK` | ![Bright black text color in terminal](/assets/images/examples/color_map/bright_black_full_text_167x16.png) |
| - | - | `BrightColor.OFF` | - |

## Background Colors
### Getting Started
#### Full Terminal Output
How to print a full line of text with colored background in the terminal:

```python
from colorist import bg_green, bg_yellow, bg_red

bg_green("This is GREEN background!")
bg_yellow("This is YELLOW background!")
bg_red("This is RED background!")
```

How it appears in the terminal:

![Example of terminal message with green, yellow, red background color](/assets/images/examples/bg_color_full_text_green_yellow_red.png)

#### Custom Terminal Output
How to customize terminal messages and change background color inside a paragraph:

```python
from colorist import BgColor

print(f"I want {BgColor.RED}red{BgColor.OFF} background color inside this paragraph")

print(f"Both {BgColor.GREEN}green{BgColor.OFF} and {BgColor.YELLOW}yellow{BgColor.OFF} are nice background colors")
```

How it appears in the terminal:

![Example of terminal message with green, yellow, red background color](/assets/images/examples/bg_color_custom_text_green_yellow_red.png)

```python
from colorist import BgBrightColor

print(f"I want {BgBrightColor.CYAN}cyan{BgBrightColor.OFF} background color inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with cyan background color](/assets/images/examples/bg_bright_color_custom_text_cyan.png)

As with text colors, remember to use `BgColor.OFF` or `BgBrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise the color may spill over and into other terminal messages.

### Supported Background Colors
| Color | Full Text Function | Custom | Example |
| ----- | ------------------ | ------ | ------- |
| ![Green](/assets/images/colors/green_16x16.png) | `bg_green("text")` | `BgColor.GREEN` | ![Green background color in terminal](/assets/images/examples/bg_color_map/green_full_text_194x16.png) |
| ![Yellow](/assets/images/colors/yellow_16x16.png) | `bg_yellow("text")` | `BgColor.YELLOW` | ![Yellow background color in terminal](/assets/images/examples/bg_color_map/yellow_full_text_194x16.png) |
| ![Red](/assets/images/colors/red_16x16.png) | `bg_red("text")` | `BgColor.RED` | ![Red background color in terminal](/assets/images/examples/bg_color_map/red_full_text_194x16.png) |
| ![Magenta](/assets/images/colors/magenta_16x16.png) | `bg_magenta("text")` | `BgColor.MAGENTA` | ![Magenta background color in terminal](/assets/images/examples/bg_color_map/magenta_full_text_194x16.png) |
| ![Blue](/assets/images/colors/blue_16x16.png) | `bg_blue("text")` | `BgColor.BLUE` | ![Blue background color in terminal](/assets/images/examples/bg_color_map/blue_full_text_194x16.png) |
| ![Cyan](/assets/images/colors/cyan_16x16.png) | `bg_cyan("text")` | `BgColor.CYAN` | ![Cyan background color in terminal](/assets/images/examples/bg_color_map/cyan_full_text_194x16.png) |
| ![White](/assets/images/colors/white_16x16.png) | `bg_white("text")` | `BgColor.WHITE` | ![White background color in terminal](/assets/images/examples/bg_color_map/white_full_text_194x16.png) |
| ![Black](/assets/images/colors/black_16x16.png) | `bg_black("text")` | `BgColor.BLACK` | ![Black background color in terminal](/assets/images/examples/bg_color_map/black_full_text_194x16.png) |
| - | - | `BgColor.OFF` | - |
| ![Bright green](/assets/images/colors/bright_green_16x16.png) | `bg_bright_green("text")` | `BgBrightColor.GREEN` | ![Bright green background color in terminal](/assets/images/examples/bg_color_map/bright_green_full_text_194x16.png) |
| ![Bright yellow](/assets/images/colors/bright_yellow_16x16.png) | `bg_bright_yellow("text")` | `BgBrightColor.YELLOW` | ![Bright yellow background color in terminal](/assets/images/examples/bg_color_map/bright_yellow_full_text_194x16.png) |
| ![Bright red](/assets/images/colors/bright_red_16x16.png) | `bg_bright_red("text")` | `BgBrightColor.RED` | ![Bright red background color in terminal](/assets/images/examples/bg_color_map/bright_red_full_text_194x16.png) |
| ![Bright magenta](/assets/images/colors/bright_magenta_16x16.png) | `bg_bright_magenta("text")` | `BgBrightColor.MAGENTA` | ![Bright magenta background color in terminal](/assets/images/examples/bg_color_map/bright_magenta_full_text_194x16.png) |
| ![Bright blue](/assets/images/colors/bright_blue_16x16.png) | `bg_bright_blue("text")` | `BgBrightColor.BLUE` | ![Bright blue background color in terminal](/assets/images/examples/bg_color_map/bright_blue_full_text_194x16.png) |
| ![Bright cyan](/assets/images/colors/bright_cyan_16x16.png) | `bg_bright_cyan("text")` | `BgBrightColor.CYAN` | ![Bright cyan background color in terminal](/assets/images/examples/bg_color_map/bright_cyan_full_text_194x16.png) |
| ![Bright white](/assets/images/colors/bright_white_16x16.png) | `bg_bright_white("text")` | `BgBrightColor.WHITE` | ![Bright white background color in terminal](/assets/images/examples/bg_color_map/bright_white_full_text_194x16.png) |
| ![Bright black](/assets/images/colors/bright_black_16x16.png) | `bg_bright_black("text")` | `BgBrightColor.BLACK` | ![Bright black background color in terminal](/assets/images/examples/bg_color_map/bright_black_full_text_194x16.png) |
| - | - | `BgBrightColor.OFF` | - |

## Effects
### Getting Started
In addition to colors, Colorist for Python can also add effects to text messages in the terminal.

#### Full Terminal Output
How to print a full line of text effect in the terminal:

```python
from colorist import effect_blink

effect_blink("This is BLINKING!")
```

How it appears in the terminal:

![Example of terminal message with blinking text](/assets/images/examples/effect_full_text_blink_default.gif)

And this can also be combined with an optional color:

```python
from colorist import Color, effect_blink

effect_blink("This is BLINKING!", Color.CYAN)
```

How it appears in the terminal:

![Example of terminal message with blinking, cyan-colored text](/assets/images/examples/effect_full_text_blink_cyan.gif)

#### Custom Terminal Output
How to customize terminal messages and change effect inside a paragraph:

```python
from colorist import Effect

print(f"I want {Effect.UNDERLINE}underlined text{Effect.UNDERLINE_OFF} inside this paragraph")

print(f"I want {Effect.BOLD}emphasized text{Effect.BOLD_OFF} inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with underline and bold text](/assets/images/examples/effect_custom_text_underline_bold.png)

Effects can also be mixed with colors:

```python
from colorist import Color, Effect

print(f"I want both {Color.RED}colored and {Effect.BLINK}blinking{Effect.BLINK_OFF} text{Color.OFF} inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with red and blinking text](/assets/images/examples/effect_custom_text_blink_red.gif)

Similar to `Color.OFF`, remember to turn off an effect with the relevant reset option (e.g `Effect.BOLD_OFF`, `Effect.DIM_OFF`, etc. or even just `Effect.OFF`) every time you want to revert back to the default terminal text style. Otherwise the effect may spill over and into other terminal messages.

### Supported Effects
| Effect           | Full Text Function         | Custom             | Reset                  | Example    |
| ---------------- | -------------------------- | ------------------ | ---------------------- | ---------- |
| **Bold**         | `effect_bold("text")`      | `Effect.BOLD`      | `Effect.BOLD_OFF`      | ![Example of terminal message with bold text](/assets/images/examples/effect_map/bold_full_text_140x16.png) |
| Dim              | `effect_dim("text")`       | `Effect.DIM`       | `Effect.DIM_OFF`       | ![Example of terminal message with dimmed text](/assets/images/examples/effect_map/dim_full_text_140x16.png) |
| <u>Underline</u> | `effect_underline("text")` | `Effect.UNDERLINE` | `Effect.UNDERLINE_OFF` | ![Example of terminal message with underlined text](/assets/images/examples/effect_map/underline_full_text_140x16.png) |
| Blink            | `effect_blink("text")`     | `Effect.BLINK`     | `Effect.BLINK_OFF`     | ![Example of terminal message with blinking text](/assets/images/examples/effect_map/blink_full_text_140x16.gif) |
| Reverse          | `effect_reverse("text")`   | `Effect.REVERSE`   | `Effect.REVERSE_OFF`   | ![Example of terminal message with reversed text color and background](/assets/images/examples/effect_map/reverse_full_text_140x16.png) |
| Hide             | `effect_hide("text")`      | `Effect.HIDE`      | `Effect.HIDE_OFF`      | ![Example of terminal message with hidden text](/assets/images/examples/effect_map/hide_full_text_140x16.png) |
| -                | -                          | -                  | `Effect.OFF`           | -          |

## Donate
This module is free to use. And if you like it, feel free to [buy me a coffee](https://github.com/sponsors/jakob-bagterp).

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/colorist-for-python/pulls).

## Report Bugs
Report bugs and issues [here](https://github.com/jakob-bagterp/colorist-for-python/issues).
