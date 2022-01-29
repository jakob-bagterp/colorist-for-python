[![Latest version](https://img.shields.io/static/v1?label=version&message=v0.1.0&color=yellowgreen)](https://github.com/jakob-bagterp/timer-for-python/releases)
![Python 3.9](https://img.shields.io/static/v1?label=python&message=v3.9&color=green)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://github.com/jakob-bagterp/timer-for-python/blob/master/LICENSE.md)

# 🌈 Colorist for Python 🌈
Make it easy and fast to print terminal messages in colors.

## Prerequisites
* Python 3.9 or higher
* macOS
    * It may work on Windows or Linux, but hasn't been tested

## Installation
### PyPI
```shell
pip3 install colorist-for-python
```

### Homebrew
If you already have installed the [Homebrew](https://brew.sh) package manager for Mac and Linux, use this terminal command to tap Colorist for Python:

```shell
brew tap jakob-bagterp/colorist-for-python
```

And then install:

```shell
brew install colorist-for-python
```

## Colors
### Getting Started
#### Full Terminal Output
How to print a full line of colored text in the terminal:

```python
from colorist import green, yellow, red

green("This is GREEN!")
yellow("This is YELLOW!")
red("This is RED!")
```

#### Custom Terminal Output
How to customize terminal messages and change color inside a paragraph:

```python
from colorist import Color

print(f"I want {Color.RED}red{Color.RESET} color inside this paragraph")

print(f"Both {Color.GREEN}green{Color.RESET} and {Color.YELLOW}yellow{Color.RESET} are nice colors")
```

```python
from colorist import BrightColor

print(f"I want {BrightColor.CYAN}cyan{BrightColor.RESET} color inside this paragraph")
```

Remember to use `Color.RESET` or `BrightColor.RESET` every time you want to revert back to the default terminal text style. Otherwise the color may spill over and into other terminal messages.

##### Other String Formats
It's easier and more readable to use f-strings as in the example above, but you can also use string addition...

```python
from colorist import Color

print("I want " + Color.RED + "red" + Color.RESET + " color inside this paragraph")
```

... or string formatting:

```python
from colorist import Color

print("I want {0}red{1} color inside this paragraph".format(Color.RED, Color.RESET))
```

### Supported Text Colors
<table>
    <tr>
        <th>Color</th>
        <th>Full Text Function</th>
        <th>Custom</th>
    </tr>
    <tr>
        <td style="background-color: rgb(78, 154, 6)">
            <img src="assets/images/colors/green_16x16.png" alt="Green">
        </td>
        <td>green("text")</td>
        <td>Color.GREEN</td>
    </tr>
    <tr>
        <td style="background-color: rgb(196, 160, 0)">
            <img src="assets/images/colors/yellow_16x16.png" alt="Yellow">
        </td>
        <td>yellow("text")</td>
        <td>Color.YELLOW</td>
    </tr>
    <tr>
        <td style="background-color: rgb(204, 0, 0)">
            <img src="assets/images/colors/red_16x16.png" alt="Red">
        </td>
        <td>red("text")</td>
        <td>Color.RED</td>
    </tr>
    <tr>
        <td style="background-color: rgb(117, 80, 123)">
            <img src="assets/images/colors/magenta_16x16.png" alt="Magenta">
        </td>
        <td>magenta("text")</td>
        <td>Color.MAGENTA</td>
    </tr>
    <tr>
        <td style="background-color: rgb(114, 159, 207)">
            <img src="assets/images/colors/blue_16x16.png" alt="Blue">
        </td>
        <td>blue("text")</td>
        <td>Color.BLUE</td>
    </tr>
    <tr>
        <td style="background-color: rgb(6, 152, 154)">
            <img src="assets/images/colors/cyan_16x16.png" alt="Cyan">
        </td>
        <td>cyan("text")</td>
        <td>Color.CYAN</td>
    </tr>
    <tr>
        <td style="background-color: rgb(211, 215, 207)">
            <img src="assets/images/colors/white_16x16.png" alt="White">
        </td>
        <td>white("text")</td>
        <td>Color.WHITE</td>
    </tr>
    <tr>
        <td style="background-color: rgb(0, 0, 0)">
            <img src="assets/images/colors/black_16x16.png" alt="Black">
        </td>
        <td>black("text")</td>
        <td>Color.BLACK</td>
    </tr>
    <tr>
        <td style="background-color: rgb(138, 226, 52)">
            <img src="assets/images/colors/bright_green_16x16.png" alt="Bright green">
        </td>
        <td>bright_green("text")</td>
        <td>BrightColor.GREEN</td>
    </tr>
    <tr>
        <td style="background-color: rgb(252, 233, 79)">
            <img src="assets/images/colors/bright_yellow_16x16.png" alt="Bright_yellow">
        </td>
        <td>bright_yellow("text")</td>
        <td>BrightColor.YELLOW</td>
    </tr>
    <tr>
        <td style="background-color: rgb(239, 41, 41)">
            <img src="assets/images/colors/bright_red_16x16.png" alt="Bright red">
        </td>
        <td>bright_red("text")</td>
        <td>BrightColor.RED</td>
    </tr>
    <tr>
        <td style="background-color: rgb(173, 127, 168)">
            <img src="assets/images/colors/bright_magenta_16x16.png" alt="Bright magenta">
        </td>
        <td>bright_magenta("text")</td>
        <td>BrightColor.MAGENTA</td>
    </tr>
    <tr>
        <td style="background-color: rgb(50, 175, 255)">
            <img src="assets/images/colors/bright_blue_16x16.png" alt="Bright blue">
        </td>
        <td>bright_blue("text")</td>
        <td>BrightColor.BLUE</td>
    </tr>
    <tr>
        <td style="background-color: rgb(52, 226, 226)">
            <img src="assets/images/colors/bright_cyan_16x16.png" alt="Bright cyan">
        </td>
        <td>bright_cyan("text")</td>
        <td>BrightColor.CYAN</td>
    </tr>
    <tr>
        <td style="background-color: rgb(255, 255, 255)">
            <img src="assets/images/colors/bright_white_16x16.png" alt="Bright white">
        </td>
        <td>bright_white("text")</td>
        <td>BrightColor.WHITE</td>
    </tr>
    <tr>
        <td style="background-color: rgb(85, 87, 83)">
            <img src="assets/images/colors/bright_black_16x16.png" alt="Bright black">
        </td>
        <td>bright_black("text")</td>
        <td>BrightColor.BLACK</td>
    </tr>
</table>

## Effects
### Getting Started
In addition to colors, Colorist for Python can also add effects to text messages in the terminal. Example:

```python
from colorist import Effect

print(f"I want {Effect.UNDERLINE}underlined text{Effect.RESET_UNDERLINE} inside this paragraph")

print(f"I want {Effect.BOLD}emphasized text{Effect.RESET_BOLD} inside this paragraph")
```

Effects can also be mixed with colors:

```python
from colorist import Color, Effect

print(f"I want both {Color.RED}colored and {Effect.BLINK}blinking{Effect.RESET_BLINK} text{Color.RESET} inside this paragraph")
```

Similar to `Color.RESET` and `BrightColor.RESET`, remember to turn off an effect with the relevant reset option (e.g `Effect.RESET_BOLD`, `Effect.RESET_BOLD`, etc. or even just `Effect.RESET_ALL`) every time you want to revert back to the default terminal text style. Otherwise the effect may spill over and into other terminal messages.

### Supported Effects
| Effect           | Full Text Function       | Custom           | Reset                  |
| ---------------- | ------------------------ | ---------------- | ---------------------- |
| **Bold**         | effect_bold("text")      | Effect.BOLD      | Effect.RESET_BOLD      |
| Dim              | effect_dim("text")       | Effect.DIM       | Effect.RESET_DIM       |
| <u>Underline</u> | effect_underline("text") | Effect.UNDERLINE | Effect.RESET_UNDERLINE |
| Blink            | effect_blink("text")     | Effect.BLINK     | Effect.RESET_BLINK     |
| Reverse          | effect_reverse("text")   | Effect.REVERSE   | Effect.RESET_REVERSE   |
| Hide             | effect_hide("text")      | Effect.HIDE      | Effect.RESET_HIDE      |
| -                | -                        | -                | Effect.RESET_ALL       |

## Donate
This module is free to use. And if you like it, feel free to [buy me a coffee](https://github.com/sponsors/jakob-bagterp).

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/colorist-for-python/pulls).

## Report Bugs
Report bugs and issues [here](https://github.com/jakob-bagterp/colorist-for-python/issues).
