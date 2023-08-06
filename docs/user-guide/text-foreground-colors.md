---
tags:
    - Features
    - Tutorial
---

# Text Foreground Colors
## Introduction
When you want to print colored text in the terminal, Colorist offers two ways of doing so:

* **Full text functions:** Print a full line of colored text with the `green()`, `yellow()`, `red()`, etc. functions.
* **Custom string styling:** Mix colors to any part of a string with the `Color` and `BrightColor` classes.

## Print Line of Colored Text
How to print a full line of colored text in the terminal:

```python linenums="1"
from colorist import green, yellow, red

green("This is GREEN!")
yellow("This is YELLOW!")
red("This is RED!")
```

How it appears in the terminal:

![Example of full line of green, yellow, red colored text printed in a terminal window](../assets/images/examples/color_full_text_green_yellow_red.png)

## Print Mixed Colors in Text
How to customize colors inside a paragraph and print it in the terminal:

```python linenums="1"
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")

print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
```

How it appears in the terminal:

![Example of white text mixed with green, yellow, red colors printed in a terminal window](../assets/images/examples/color_custom_text_green_yellow_red.png)

!!! tip
    Remember to turn off a color with `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## Bright Colors
Most terminals support bright colors that stand more out:

```python linenums="1"
from colorist import BrightColor

print(f"I want {BrightColor.CYAN}cyan{BrightColor.OFF} color inside this paragraph")
```

How it appears in the terminal:

![Example of white text mixed with cyan printed in a terminal window](../assets/images/examples/bright_color_custom_text_cyan.png)

For a complete list of full text color functions and custom string styling, refer to the [documentation](../reference/text-foreground-colors.md).
