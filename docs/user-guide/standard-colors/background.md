---
title: How to Add Background Colors to Text
description: The easiest way to print colored background text in terminal output using Colorist for Python. Includes code examples.
tags:
    - Features
    - Tutorial
    - Background Colors
    - Standard Colors
---

# How to Print Background Colors
## Introduction
When you want to print colored backgrounds in the terminal, Colorist offers two ways of doing so:

* **Full text functions:** Print a full line of colored text with the `bg_green()`, `bg_yellow()`, `bg_red()`, etc. functions.
* **Custom string styling:** Mix colors to any part of a string with the `BgColor` and `BgBrightColor` classes.

## Print Line of Text with Background Color
How to print a full line of colored text in the terminal:

```python linenums="1" hl_lines="3-5"
from colorist import bg_green, bg_yellow, bg_red

bg_green("This is GREEN background!")
bg_yellow("This is YELLOW background!")
bg_red("This is RED background!")
```

How it appears in the terminal:

<pre><code>% <span class="bg-green text-contrast">This is GREEN background!</span>
% <span class="bg-yellow text-contrast">This is YELLOW background!</span>
% <span class="bg-red text-contrast">This is RED background!</span></code></pre>

Refer to the documetation for a [complete list of color options](../../reference/background-colors/full-line.md).

## Print Mixed Colors in Text
Background colors can also be mixed inside a paragraph:

```python linenums="1" hl_lines="3-5"
from colorist import BgColor

print(f"Put {BgColor.RED}RED{BgColor.OFF} background color inside this paragraph")
print(f"Both {BgColor.GREEN}GREEN{BgColor.OFF}...")
print(f"... and {BgColor.YELLOW}YELLOW{BgColor.OFF} are nice background colors")
```

How it appears in the terminal:

<pre><code>% Put <span class="bg-red text-contrast">RED</span> background color inside this paragraph
% Both <span class="bg-green text-contrast">GREEN</span>...
% ... and <span class="bg-yellow text-contrast">YELLOW</span> are nice background colors</code></pre>

!!! tip
    Remember to turn off a color with `BgColor.OFF` or `BgBrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## Bright Colors
Most terminals support bright colors that stand more out:

```python linenums="1" hl_lines="3"
from colorist import BgBrightColor

print(f"Add {BgBrightColor.CYAN}CYAN{BgBrightColor.OFF} background color")
```

How it appears in the terminal:

<pre><code>% Add <span class="bg-bright-cyan text-contrast">CYAN</span> background color</code></pre>

Refer to the documetation for a [complete list of color options for custom background styling](../../reference/background-colors/mixed.md).

## Cheat Sheets
### Normal Colors

| Color                                                    | Color Code        | Example                                                                                |
| -------------------------------------------------------- | ----------------- | -------------------------------------------------------------------------------------- |
| ![Green](../../assets/images/colors/green_16x16.png)     | `BgColor.GREEN`   | <code><span class="bg-green text-contrast">This is GREEN background!</span></code>     |
| ![Yellow](../../assets/images/colors/yellow_16x16.png)   | `BgColor.YELLOW`  | <code><span class="bg-yellow text-contrast">This is YELLOW background!</span></code>   |
| ![Red](../../assets/images/colors/red_16x16.png)         | `BgColor.RED`     | <code><span class="bg-red text-contrast">This is RED background!</span></code>         |
| ![Magenta](../../assets/images/colors/magenta_16x16.png) | `BgColor.MAGENTA` | <code><span class="bg-magenta text-contrast">This is MAGENTA background!</span></code> |
| ![Blue](../../assets/images/colors/blue_16x16.png)       | `BgColor.BLUE`    | <code><span class="bg-blue text-contrast">This is BLUE background!</span></code>       |
| ![Cyan](../../assets/images/colors/cyan_16x16.png)       | `BgColor.CYAN`    | <code><span class="bg-cyan text-contrast">This is CYAN background!</span></code>       |
| ![White](../../assets/images/colors/white_16x16.png)     | `BgColor.WHITE`   | <code><span class="bg-white text-contrast">This is WHITE background!</span></code>     |
| ![Black](../../assets/images/colors/black_16x16.png)     | `BgColor.BLACK`   | <code><span class="bg-black text-contrast">This is BLACK background!</span></code>     |
| -                                                        | `BgColor.DEFAULT` | -                                                                                      |
| -                                                        | `BgColor.OFF`     | -                                                                                      |

### Bright Colors

| Color                                                                  | Color Code              | Example                                                                                              |
| ---------------------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------- |
| ![Bright green](../../assets/images/colors/bright_green_16x16.png)     | `BgBrightColor.GREEN`   | <code><span class="bg-bright-green text-contrast">This is BRIGHT GREEN background!</span></code>     |
| ![Bright yellow](../../assets/images/colors/bright_yellow_16x16.png)   | `BgBrightColor.YELLOW`  | <code><span class="bg-bright-yellow text-contrast">This is BRIGHT YELLOW background!</span></code>   |
| ![Bright red](../../assets/images/colors/bright_red_16x16.png)         | `BgBrightColor.RED`     | <code><span class="bg-bright-red text-contrast">This is BRIGHT RED background!</span></code>         |
| ![Bright magenta](../../assets/images/colors/bright_magenta_16x16.png) | `BgBrightColor.MAGENTA` | <code><span class="bg-bright-magenta text-contrast">This is BRIGHT MAGENTA background!</span></code> |
| ![Bright blue](../../assets/images/colors/bright_blue_16x16.png)       | `BgBrightColor.BLUE`    | <code><span class="bg-bright-blue text-contrast">This is BRIGHT BLUE background!</span></code>       |
| ![Bright cyan](../../assets/images/colors/bright_cyan_16x16.png)       | `BgBrightColor.CYAN`    | <code><span class="bg-bright-cyan text-contrast">This is BRIGHT CYAN background!</span></code>       |
| ![Bright white](../../assets/images/colors/bright_white_16x16.png)     | `BgBrightColor.WHITE`   | <code><span class="bg-bright-white text-contrast">This is BRIGHT WHITE background!</span></code>     |
| ![Bright black](../../assets/images/colors/bright_black_16x16.png)     | `BgBrightColor.BLACK`   | <code><span class="bg-bright-black text-contrast">This is BRIGHT BLACK background!</span></code>     |
| -                                                                      | `BgBrightColor.DEFAULT` | -                                                                                                    |
| -                                                                      | `BgBrightColor.OFF`     | -                                                                                                    |
