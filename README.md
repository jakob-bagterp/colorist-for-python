[![Latest version](https://img.shields.io/static/v1?label=version&message=1.1.2&color=yellowgreen)](https://github.com/jakob-bagterp/colorist-for-python/releases)
![Python >=3.9](https://img.shields.io/static/v1?label=python&message=>=3.9&color=green)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blueviolet)](https://github.com/jakob-bagterp/colorist-for-python/blob/master/LICENSE.md)

# 🌈 Colorist for Python 🌈
Lightweight Python package that makes it easy and fast to print terminal messages in colors.

## Prerequisites
* Python 3.9 or higher
* macOS
    * It may work on Windows or Linux, but hasn't been tested

## Installation
### PyPI
```shell
pip3 install colorist
```

### Homebrew
If you already have installed the [Homebrew](https://brew.sh) package manager for Mac and Linux, use this terminal command to tap Colorist for Python:

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

![Example of terminal message with green, yellow, red text color](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_full_text_green_yellow_red.png)

#### Custom Terminal Output
How to customize terminal messages and change color inside a paragraph:

```python
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")

print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
```

How it appears in the terminal:

![Example of terminal message with green, yellow, red text color](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_custom_text_green_yellow_red.png)


```python
from colorist import BrightColor

print(f"I want {BrightColor.CYAN}cyan{BrightColor.OFF} color inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with cyan text color](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bright_color_custom_text_cyan.png)

Remember to use `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise the color may spill over and into other terminal messages.

##### Other String Formats
It's easier and more readable to use f-strings as in the examples above, but you can also use string format:

```python
from colorist import Color

print("I want {0}red{1} color inside this paragraph".format(Color.RED, Color.OFF))
```

How it appears in the terminal:

![Example of terminal message with red text color](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_custom_text_red.png)

### Supported Text Colors
<table>
    <tr>
        <th>Color</th>
        <th>Full Text Function</th>
        <th>Custom</th>
        <th>Example</th>
    </tr>
    <tr>
        <td style="background-color: rgb(78, 154, 6)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/green_16x16.png" alt="Green">
        </td>
        <td>green("text")</td>
        <td>Color.GREEN</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/green_full_text_167x16.png" alt="Green text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(196, 160, 0)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/yellow_16x16.png" alt="Yellow">
        </td>
        <td>yellow("text")</td>
        <td>Color.YELLOW</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/yellow_full_text_167x16.png" alt="Yellow text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(204, 0, 0)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/red_16x16.png" alt="Red">
        </td>
        <td>red("text")</td>
        <td>Color.RED</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/red_full_text_167x16.png" alt="Red text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(117, 80, 123)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/magenta_16x16.png" alt="Magenta">
        </td>
        <td>magenta("text")</td>
        <td>Color.MAGENTA</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/magenta_full_text_167x16.png" alt="Magenta text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(114, 159, 207)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/blue_16x16.png" alt="Blue">
        </td>
        <td>blue("text")</td>
        <td>Color.BLUE</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/blue_full_text_167x16.png" alt="Blue text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(6, 152, 154)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/cyan_16x16.png" alt="Cyan">
        </td>
        <td>cyan("text")</td>
        <td>Color.CYAN</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/cyan_full_text_167x16.png" alt="Cyan text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(211, 215, 207)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/white_16x16.png" alt="White">
        </td>
        <td>white("text")</td>
        <td>Color.WHITE</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/white_full_text_167x16.png" alt="White text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(0, 0, 0)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/black_16x16.png" alt="Black">
        </td>
        <td>black("text")</td>
        <td>Color.BLACK</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/black_full_text_167x16.png" alt="Black text color in terminal">
        </td>
    </tr>
    <tr>
        <td>-</td>
        <td>-</td>
        <td>Color.OFF</td>
        <td>-</td>
    </tr>
    <tr>
        <td style="background-color: rgb(138, 226, 52)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_green_16x16.png" alt="Bright green">
        </td>
        <td>bright_green("text")</td>
        <td>BrightColor.GREEN</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/bright_green_full_text_167x16.png" alt="Bright green text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(252, 233, 79)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_yellow_16x16.png" alt="Bright yellow">
        </td>
        <td>bright_yellow("text")</td>
        <td>BrightColor.YELLOW</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/bright_yellow_full_text_167x16.png" alt="Bright yellow text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(239, 41, 41)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_red_16x16.png" alt="Bright red">
        </td>
        <td>bright_red("text")</td>
        <td>BrightColor.RED</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/bright_red_full_text_167x16.png" alt="Bright red text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(173, 127, 168)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_magenta_16x16.png" alt="Bright magenta">
        </td>
        <td>bright_magenta("text")</td>
        <td>BrightColor.MAGENTA</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/bright_magenta_full_text_167x16.png" alt="Bright magenta text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(50, 175, 255)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_blue_16x16.png" alt="Bright blue">
        </td>
        <td>bright_blue("text")</td>
        <td>BrightColor.BLUE</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/bright_blue_full_text_167x16.png" alt="Bright blue text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(52, 226, 226)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_cyan_16x16.png" alt="Bright cyan">
        </td>
        <td>bright_cyan("text")</td>
        <td>BrightColor.CYAN</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/bright_cyan_full_text_167x16.png" alt="Bright cyan text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(255, 255, 255)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_white_16x16.png" alt="Bright white">
        </td>
        <td>bright_white("text")</td>
        <td>BrightColor.WHITE</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/bright_white_full_text_167x16.png" alt="Bright white text color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(85, 87, 83)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_black_16x16.png" alt="Bright black">
        </td>
        <td>bright_black("text")</td>
        <td>BrightColor.BLACK</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/color_map/bright_black_full_text_167x16.png" alt="Bright black text color in terminal">
        </td>
    </tr>
    <tr>
        <td>-</td>
        <td>-</td>
        <td>BrightColor.OFF</td>
        <td>-</td>
    </tr>
</table>

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

![Example of terminal message with green, yellow, red background color](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_full_text_green_yellow_red.png)

#### Custom Terminal Output
How to customize terminal messages and change background color inside a paragraph:

```python
from colorist import BgColor

print(f"I want {BgColor.RED}red{BgColor.OFF} background color inside this paragraph")

print(f"Both {BgColor.GREEN}green{BgColor.OFF} and {BgColor.YELLOW}yellow{BgColor.OFF} are nice background colors")
```

How it appears in the terminal:

![Example of terminal message with green, yellow, red background color](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_custom_text_green_yellow_red.png)

```python
from colorist import BgBrightColor

print(f"I want {BgBrightColor.CYAN}cyan{BgBrightColor.OFF} background color inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with cyan background color](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_bright_color_custom_text_cyan.png)

As with text colors, remember to use `BgColor.OFF` or `BgBrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise the color may spill over and into other terminal messages.

### Supported Background Colors
<table>
    <tr>
        <th>Color</th>
        <th>Full Text Function</th>
        <th>Custom</th>
        <th>Example</th>
    </tr>
    <tr>
        <td style="background-color: rgb(78, 154, 6)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/green_16x16.png" alt="Green">
        </td>
        <td>bg_green("text")</td>
        <td>BgColor.GREEN</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/green_full_text_194x16.png" alt="Green background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(196, 160, 0)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/yellow_16x16.png" alt="Yellow">
        </td>
        <td>bg_yellow("text")</td>
        <td>BgColor.YELLOW</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/yellow_full_text_194x16.png" alt="Yellow background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(204, 0, 0)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/red_16x16.png" alt="Red">
        </td>
        <td>bg_red("text")</td>
        <td>BgColor.RED</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/red_full_text_194x16.png" alt="Red background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(117, 80, 123)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/magenta_16x16.png" alt="Magenta">
        </td>
        <td>bg_magenta("text")</td>
        <td>BgColor.MAGENTA</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/magenta_full_text_194x16.png" alt="Magenta background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(114, 159, 207)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/blue_16x16.png" alt="Blue">
        </td>
        <td>bg_blue("text")</td>
        <td>BgColor.BLUE</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/blue_full_text_194x16.png" alt="Blue background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(6, 152, 154)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/cyan_16x16.png" alt="Cyan">
        </td>
        <td>bg_cyan("text")</td>
        <td>BgColor.CYAN</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/cyan_full_text_194x16.png" alt="Cyan background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(211, 215, 207)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/white_16x16.png" alt="White">
        </td>
        <td>bg_white("text")</td>
        <td>BgColor.WHITE</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/white_full_text_194x16.png" alt="White background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(0, 0, 0)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/black_16x16.png" alt="Black">
        </td>
        <td>bg_black("text")</td>
        <td>BgColor.BLACK</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/black_full_text_194x16.png" alt="Black background color in terminal">
        </td>
    </tr>
    <tr>
        <td>-</td>
        <td>-</td>
        <td>BgColor.OFF</td>
        <td>-</td>
    </tr>
    <tr>
        <td style="background-color: rgb(138, 226, 52)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_green_16x16.png" alt="Bright green">
        </td>
        <td>bg_bright_green("text")</td>
        <td>BgBrightColor.GREEN</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/bright_green_full_text_194x16.png" alt="Bright green background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(252, 233, 79)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_yellow_16x16.png" alt="Bright yellow">
        </td>
        <td>bg_bright_yellow("text")</td>
        <td>BgBrightColor.YELLOW</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/bright_yellow_full_text_194x16.png" alt="Bright yellow background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(239, 41, 41)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_red_16x16.png" alt="Bright red">
        </td>
        <td>bg_bright_red("text")</td>
        <td>BgBrightColor.RED</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/bright_red_full_text_194x16.png" alt="Bright red background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(173, 127, 168)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_magenta_16x16.png" alt="Bright magenta">
        </td>
        <td>bg_bright_magenta("text")</td>
        <td>BgBrightColor.MAGENTA</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/bright_magenta_full_text_194x16.png" alt="Bright magenta background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(50, 175, 255)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_blue_16x16.png" alt="Bright blue">
        </td>
        <td>bg_bright_blue("text")</td>
        <td>BgBrightColor.BLUE</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/bright_blue_full_text_194x16.png" alt="Bright blue background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(52, 226, 226)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_cyan_16x16.png" alt="Bright cyan">
        </td>
        <td>bg_bright_cyan("text")</td>
        <td>BgBrightColor.CYAN</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/bright_cyan_full_text_194x16.png" alt="Bright cyan background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(255, 255, 255)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_white_16x16.png" alt="Bright white">
        </td>
        <td>bg_bright_white("text")</td>
        <td>BgBrightColor.WHITE</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/bright_white_full_text_194x16.png" alt="Bright white background color in terminal">
        </td>
    </tr>
    <tr>
        <td style="background-color: rgb(85, 87, 83)">
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/colors/bright_black_16x16.png" alt="Bright black">
        </td>
        <td>bg_bright_black("text")</td>
        <td>BgBrightColor.BLACK</td>
        <td>
            <img src="https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/bg_color_map/bright_black_full_text_194x16.png" alt="Bright black background color in terminal">
        </td>
    </tr>
    <tr>
        <td>-</td>
        <td>-</td>
        <td>BgBrightColor.OFF</td>
        <td>-</td>
    </tr>
</table>

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

![Example of terminal message with blinking text](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_full_text_blink_default.gif)

And this can also be combined with an optional color:

```python
from colorist import Color, effect_blink

effect_blink("This is BLINKING!", Color.CYAN)
```

How it appears in the terminal:

![Example of terminal message with blinking, cyan-colored text](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_full_text_blink_cyan.gif)

#### Custom Terminal Output
How to customize terminal messages and change effect inside a paragraph:

```python
from colorist import Effect

print(f"I want {Effect.UNDERLINE}underlined text{Effect.UNDERLINE_OFF} inside this paragraph")

print(f"I want {Effect.BOLD}emphasized text{Effect.BOLD_OFF} inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with underline and bold text](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_custom_text_underline_bold.png)

Effects can also be mixed with colors:

```python
from colorist import Color, Effect

print(f"I want both {Color.RED}colored and {Effect.BLINK}blinking{Effect.BLINK_OFF} text{Color.OFF} inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with red and blinking text](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_custom_text_blink_red.gif)

Similar to `Color.OFF`, remember to turn off an effect with the relevant reset option (e.g `Effect.BOLD_OFF`, `Effect.DIM_OFF`, etc. or even just `Effect.OFF`) every time you want to revert back to the default terminal text style. Otherwise the effect may spill over and into other terminal messages.

### Supported Effects
| Effect           | Full Text Function       | Custom           | Reset                | Example    |
| ---------------- | ------------------------ | ---------------- | -------------------- | ---------- |
| **Bold**         | effect_bold("text")      | Effect.BOLD      | Effect.BOLD_OFF      | ![Example of terminal message with bold text](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_map/bold_full_text_140x16.png) |
| Dim              | effect_dim("text")       | Effect.DIM       | Effect.DIM_OFF       | ![Example of terminal message with dimmed text](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_map/dim_full_text_140x16.png) |
| <u>Underline</u> | effect_underline("text") | Effect.UNDERLINE | Effect.UNDERLINE_OFF | ![Example of terminal message with underlined text](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_map/underline_full_text_140x16.png) |
| Blink            | effect_blink("text")     | Effect.BLINK     | Effect.BLINK_OFF     | ![Example of terminal message with blinking text](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_map/blink_full_text_140x16.gif) |
| Reverse          | effect_reverse("text")   | Effect.REVERSE   | Effect.REVERSE_OFF   | ![Example of terminal message with reversed text color and background](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_map/reverse_full_text_140x16.png) |
| Hide             | effect_hide("text")      | Effect.HIDE      | Effect.HIDE_OFF      | ![Example of terminal message with hidden text](https://github.com/jakob-bagterp/colorist-for-python/blob/master/assets/images/examples/effect_map/hide_full_text_140x16.png) |
| -                | -                        | -                | Effect.OFF           | -          |

## Donate
This module is free to use. And if you like it, feel free to [buy me a coffee](https://github.com/sponsors/jakob-bagterp).

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/colorist-for-python/pulls).

## Report Bugs
Report bugs and issues [here](https://github.com/jakob-bagterp/colorist-for-python/issues).
