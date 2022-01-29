[![Latest version](https://img.shields.io/static/v1?label=version&message=v0.3.4&color=yellowgreen)](https://github.com/jakob-bagterp/timer-for-python/releases)
![Python 3.4](https://img.shields.io/static/v1?label=python&message=v3.4&color=green)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://github.com/jakob-bagterp/timer-for-python/blob/master/LICENSE.md)

# 🌈 Colorist for Python 🌈
Make it easy and fast to print terminal messages in colors.

## Prerequisites
* Python 3.4 or higher
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

## Getting Started
### Full Terminal Output
How to print a full line of colored text in the terminal:

```python
from colorist import green, yellow, red

green("This is GREEN!")
yellow("This is YELLOW!")
red("This is RED!")
```

### Custom Terminal Output
How to customize terminal messages and change color inside a paragraph:

```python
from colorist import Color

print(f"I want {Color.RED}red{Color.RESET} color inside this paragraph")

print(f"I can't decide whether {Color.GREEN}green{Color.RESET} or {Color.YELLOW}yellow{Color.RESET} is better")
```

Remember to use the `Color.RESET` every time you want to revert back to the default terminal text color. Otherwise the color may spill over and into other terminal messages.

#### Other String Formats
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

## Supported Colors
<table>
    <tr>
        <th>Color</th>
        <th>Full</th>
        <th>Custom</th>
    </tr>
    <tr>
        <td style="background-color: rgb(78, 154, 6)"></td>
        <td>green("text")</td>
        <td>Color.GREEN</td>
    </tr>
    <tr>
        <td style="background-color: rgb(196, 160, 0)"></td>
        <td>yellow("text")</td>
        <td>Color.YELLOW</td>
    </tr>
    <tr>
        <td style="background-color: rgb(204, 0, 0)"></td>
        <td>red("text")</td>
        <td>Color.RED</td>
    </tr>
    <tr>
        <td style="background-color: rgb(117, 80, 123)"></td>
        <td>magenta("text")</td>
        <td>Color.MAGENTA</td>
    </tr>
</table>

## Donate
This module is free to use. And if you like it, feel free to [buy me a coffee](https://github.com/sponsors/jakob-bagterp).

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/colorist-for-python/pulls).

## Report Bugs
Report bugs and issues [here](https://github.com/jakob-bagterp/colorist-for-python/issues).
