---
title: How to Add RGB Colors to Text
description: The easiest way to print text with 24-bit RGB colors in terminal output using Colorist for Python. Includes code examples.
tags:
    - Features
    - Tutorial
    - Extended Colors
    - RGB Colors
---

# RGB Colors
## What are RGB Colors?
The 24-bit RGB color model covers over 16 million colors, and each color can be defined as red, green, and blue:

| Channel        | Red     | Green   | Blue    |
| -------------- | :-----: | :-----: | :-----: |
| Allowed values | `0-255` | `0-255` | `0-255` |

!!! info "Disclaimer"
    Not all [terminals support](../compatibility/terminal-support.md) 24-bit colors in RGB, HSL, or Hex. If your terminal does support such advanced colors, read on.

<div class="cubes">
    <img src="../../../assets/images/cube/cube_bright.svg" alt="Color cube bright">
    <img src="../../../assets/images/cube/cube_dark.svg" alt="Color cube dark">
</div>

## Full Line Text Functions
Try the `rgb()` and `bg_rgb()` methods for a full line of colored text. The values for red, green, blue can be an integer between `0`-`255`.

Example:

```python linenums="1" hl_lines="3-4"
from colorist import rgb, bg_rgb

rgb("I want this text in blue RGB colors", 0, 128, 255)
bg_rgb("I want this background in blue RGB colors", 0, 128, 255)
```

How it appears in the terminal:

<pre><code>% <span style="color: rgb(0, 128, 255)">I want this text in blue RGB colors</span>
% <span class="text-contrast" style="background-color: rgb(0, 128, 255)">I want this background in blue RGB colors</span></code></pre>

## Custom String Styling
Or customize the styling of text and background with the `ColorRGB()` and `BgColorRGB()` classes:

```python linenums="1" hl_lines="6-7"
from colorist import ColorRGB, BgColorRGB

dusty_pink = ColorRGB(194, 145, 164)
bg_steel_blue = BgColorRGB(70, 130, 180)

print(f"I want to use {dusty_pink}DUSTY PINK{dusty_pink.OFF}...")
print(f"... and {bg_steel_blue}STEEL BLUE{bg_steel_blue.OFF} colors")
```

How it appears in the terminal:

<pre><code>% I want to use <span style="color: rgb(194, 145, 164)">DUSTY PINK</span>...
% ... and <span class="text-contrast" style="background-color: rgb(70, 130, 180)">STEEL BLUE</span> colors</code></pre>
