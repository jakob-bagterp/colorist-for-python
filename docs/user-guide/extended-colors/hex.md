---
title: How to Add Hex Colors to Text
description: The easiest way to print text with 24-bit RGB colors in terminal output using Hex codes and Colorist for Python. Includes code examples.
tags:
    - Features
    - Tutorial
    - Extended Colors
    - Hex Colors
---

# Hex Colors
## What are Hex Colors?
The 24-bit Hex color model covers over 16 million colors, and each color can be defined with a code in hexadecimal, for instance `#00aaff` or sometimes shortened to `#0af`, that can be broken down into a [RGB value](rgb.md):

| Hex Code  | `00`  | `aa`  | `ff`  |
| --------- | :---: | :---: | :---: |
| RGB value | `0`   | `170` | `255` |
| Channel   | Red   | Green | Blue  |

!!! info "Disclaimer"
    Not all [terminals support](../compatibility/terminal-support.md) 24-bit colors in RGB, HSL, or Hex. If your terminal does support such advanced colors, read on.

<div class="color-cubes">
    <img src="../../../assets/images/cubes/cube_bright.svg" alt="Color cube bright">
    <img src="../../../assets/images/cubes/cube_dark.svg" alt="Color cube dark">
</div>

## Full Line Text Functions
Try the `hex()` and `bg_hex()` methods for a full line of colored text. Allowed Hex values are, for instance, `#00aaff` or `#0af`, alternatively without the hash sign as `00aaff` or `0af`.

Example:

```python linenums="1" hl_lines="3-4"
from colorist import hex, bg_hex

hex("I want this text in coral Hex colors", "#ff7f50")
bg_hex("I want this background in coral Hex colors", "#ff7f50")
```

How it appears in the terminal:

<pre><code>% <span style="color: #ff7f50">I want this text in coral Hex colors</span>
% <span class="text-contrast" style="background-color: #ff7f50">I want this background in coral Hex colors</span></code></pre>

## Custom String Styling
Or customize the styling of text and background with the `ColorHex()` and `BgColorHex()` classes:

```python linenums="1" hl_lines="6-7"
from colorist import ColorHex, BgColorHex

watermelon_red = ColorHex("#ff5733")
bg_mint_green = BgColorHex("#99ff99")

print(f"I want to use {watermelon_red}WATERMELON RED{watermelon_red.OFF}...")
print(f"... and {bg_mint_green}MINT GREEN{bg_mint_green.OFF} colors")
```

How it appears in the terminal:

<pre><code>% I want to use <span style="color: #ff5733">WATERMELON RED</span>...
% ... and <span class="text-contrast" style="background-color: #99ff99">MINT GREEN</span> colors</code></pre>
