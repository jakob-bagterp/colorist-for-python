---
tags:
    - Features
    - Tutorial
---

# Background Colors
## Introduction
When you want to print colored backgrounds in the terminal, Colorist offers two ways of doing so:

* **Full text functions:** Print a full line of colored text with the `bg_green()`, `bg_yellow()`, `bg_red()`, etc. functions.
* **Custom string styling:** Mix colors to any part of a string with the `BgColor` and `BgBrightColor` classes.

## Print Line of Text with Background Color
How to print a full line of colored text in the terminal:

```python linenums="1"
from colorist import bg_green, bg_yellow, bg_red

bg_green("This is GREEN background!")
bg_yellow("This is YELLOW background!")
bg_red("This is RED background!")
```

How it appears in the terminal:

![Example of white text and colored backgrounds if green, yellow, red printed in a terminal window](../assets/images/examples/bg_color_full_text_green_yellow_red.png)

## Print Mixed Colors in Text
Background colors can also be mixed inside a paragraph:

```python linenums="1"
from colorist import BgColor

print(f"I want {BgColor.RED}red{BgColor.OFF} background color inside this paragraph")

print(f"Both {BgColor.GREEN}green{BgColor.OFF} and {BgColor.YELLOW}yellow{BgColor.OFF} are nice background colors")
```

How it appears in the terminal:

![Example of black, green, yellow, red background colors mixed inside paragraph printed in a terminal window](../assets/images/examples/bg_color_custom_text_green_yellow_red.png)

!!! tip
    Remember to turn off a color with `BgColor.OFF` or `BgBrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## Bright Colors
Most terminals support bright colors that stand more out:

```python linenums="1"
from colorist import BgBrightColor

print(f"I want {BgBrightColor.CYAN}cyan{BgBrightColor.OFF} background color inside this paragraph")
```

How it appears in the terminal:

![Example of white text on a cyan background color printed in a terminal window](../assets/images/examples/bg_bright_color_custom_text_cyan.png)

## Overview of Standard and Bright Colors
For a complete list of full text color functions and custom string styling, refer to the [documentation](../reference/background-colors.md).

| Color | Normal | Bright |
| ----- | :----: | :----: |
| Green | ![Green](../assets/images/colors/green_16x16.png) | ![Bright green](../assets/images/colors/bright_green_16x16.png) |
| Yellow | ![Yellow](../assets/images/colors/yellow_16x16.png) | ![Bright yellow](../assets/images/colors/bright_yellow_16x16.png) |
| Red | ![Red](../assets/images/colors/red_16x16.png) | ![Bright red](../assets/images/colors/bright_red_16x16.png) |
| Magenta | ![Magenta](../assets/images/colors/magenta_16x16.png) | ![Bright magenta](../assets/images/colors/bright_magenta_16x16.png) |
| Blue | ![Blue](../assets/images/colors/blue_16x16.png) | ![Bright blue](../assets/images/colors/bright_blue_16x16.png) |
| Cyan | ![Cyan](../assets/images/colors/cyan_16x16.png) | ![Bright cyan](../assets/images/colors/bright_cyan_16x16.png) |
| White | ![White](../assets/images/colors/white_16x16.png) | ![Bright white](../assets/images/colors/bright_white_16x16.png) |
| Black | ![Black](../assets/images/colors/black_16x16.png) | ![Bright black](../assets/images/colors/bright_black_16x16.png) |
