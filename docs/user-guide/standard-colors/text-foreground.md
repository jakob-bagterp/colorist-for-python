---
title: How to Add Foreground Colors to Text
description: The easiest way to print colored foreground text in terminal output using Colorist for Python. Includes code examples.
tags:
    - Features
    - Tutorial
    - Standard Colors
    - Text Colors
    - Foreground Colors
---

# How to Print Foreground Text Colors
## Introduction
When you want to print colored text in the terminal, Colorist offers two ways of doing so:

* **Full text functions:** Print a full line of colored text with the `green()`, `yellow()`, `red()`, etc. functions.
* **Custom string styling:** Mix colors to any part of a string with the `Color` and `BrightColor` classes.

## Print Line of Colored Text
How to print a full line of colored text in the terminal:

```python linenums="1" hl_lines="3-5"
from colorist import green, yellow, red

green("This is GREEN!")
yellow("This is YELLOW!")
red("This is RED!")
```

How it appears in the terminal:

<pre><code>% <span class="fg-green">This is GREEN!</span>
% <span class="fg-yellow">This is YELLOW!</span>
% <span class="fg-red">This is RED!</span></code></pre>

## Print Mixed Colors in Text
How to customize colors inside a paragraph and print it in the terminal:

```python linenums="1" hl_lines="3 5"
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")

print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
```

How it appears in the terminal:

<pre><code>% I want <span class="fg-red">red</span> color inside this paragraph
% Both <span class="fg-green">green</span> and <span class="fg-yellow">yellow</span> are nice colors</code></pre>

!!! tip
    Remember to turn off a color with `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## Bright Colors
Most terminals support bright colors that stand more out:

```python linenums="1" hl_lines="3"
from colorist import BrightColor

print(f"Put {BrightColor.CYAN}cyan{BrightColor.OFF} inside this paragraph")
```

How it appears in the terminal:

<pre><code>% Put <span class="fg-bright-cyan">cyan</span> inside this paragraph</code></pre>

Refer to the documentation for a complete list of [full line text color functions](../../reference/text-colors/full-line.md) and [custom string styling](../../reference/text-colors/mixed.md).

## Cheat Sheets
### Normal Colors

| Color                                                    | Color Code      | Example                                                       |
| -------------------------------------------------------- | --------------- | ------------------------------------------------------------- |
| ![Green](../../assets/images/colors/green_16x16.png)     | `Color.GREEN`   | <code><span class="fg-green">This is GREEN!</span></code>     |
| ![Yellow](../../assets/images/colors/yellow_16x16.png)   | `Color.YELLOW`  | <code><span class="fg-yellow">This is YELLOW!</span></code>   |
| ![Red](../../assets/images/colors/red_16x16.png)         | `Color.RED`     | <code><span class="fg-red">This is RED!</span></code>         |
| ![Magenta](../../assets/images/colors/magenta_16x16.png) | `Color.MAGENTA` | <code><span class="fg-magenta">This is MAGENTA!</span></code> |
| ![Blue](../../assets/images/colors/blue_16x16.png)       | `Color.BLUE`    | <code><span class="fg-blue">This is BLUE!</span></code>       |
| ![Cyan](../../assets/images/colors/cyan_16x16.png)       | `Color.CYAN`    | <code><span class="fg-cyan">This is CYAN!</span></code>       |
| ![White](../../assets/images/colors/white_16x16.png)     | `Color.WHITE`   | <code><span class="fg-white">This is WHITE!</span></code>     |
| ![Black](../../assets/images/colors/black_16x16.png)     | `Color.BLACK`   | <code><span class="fg-black">This is BLACK!</span></code>     |
| -                                                        | `Color.DEFAULT` | -                                                             |
| -                                                        | `Color.OFF`     | -                                                             |

### Bright Colors

| Color                                                                  | Color Code            | Example                                                                     |
| ---------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------------------- |
| ![Bright green](../../assets/images/colors/bright_green_16x16.png)     | `BrightColor.GREEN`   | <code><span class="fg-bright-green">This is BRIGHT GREEN!</span></code>     |
| ![Bright yellow](../../assets/images/colors/bright_yellow_16x16.png)   | `BrightColor.YELLOW`  | <code><span class="fg-bright-yellow">This is BRIGHT YELLOW!</span></code>   |
| ![Bright red](../../assets/images/colors/bright_red_16x16.png)         | `BrightColor.RED`     | <code><span class="fg-bright-red">This is BRIGHT RED!</span></code>         |
| ![Bright magenta](../../assets/images/colors/bright_magenta_16x16.png) | `BrightColor.MAGENTA` | <code><span class="fg-bright-magenta">This is BRIGHT MAGENTA!</span></code> |
| ![Bright blue](../../assets/images/colors/bright_blue_16x16.png)       | `BrightColor.BLUE`    | <code><span class="fg-bright-blue">This is BRIGHT BLUE!</span></code>       |
| ![Bright cyan](../../assets/images/colors/bright_cyan_16x16.png)       | `BrightColor.CYAN`    | <code><span class="fg-bright-cyan">This is BRIGHT CYAN!</span></code>       |
| ![Bright white](../../assets/images/colors/bright_white_16x16.png)     | `BrightColor.WHITE`   | <code><span class="fg-bright-white">This is BRIGHT WHITE!</span></code>     |
| ![Bright black](../../assets/images/colors/bright_black_16x16.png)     | `BrightColor.BLACK`   | <code><span class="fg-bright-black">This is BRIGHT BLACK!</span></code>     |
| -                                                                      | `BrightColor.DEFAULT` | -                                                                           |
| -                                                                      | `BrightColor.OFF`     | -                                                                           |
