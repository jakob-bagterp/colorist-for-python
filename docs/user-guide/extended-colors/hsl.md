---
title: How to Add HSL Colors to Text
description: The easiest way to print text with 24-bit RGB colors in terminal output using HSL and Colorist for Python. Includes code examples.
tags:
    - Features
    - Tutorial
    - Extended Colors
    - HSL Colors
---

# HSL Colors
## What are HSL Colors?
The 24-bit HSL color model covers over 16 million colors, and each color can be defined as hue, saturation, and lightness:

| Parameter      | Hue                           | Saturation                | Lightness                  |
| -------------- | :---------------------------: | :-----------------------: | :------------------------: |
| Allowed values | `0`-`360` degrees             | `0`-`100` %               | `0`-`100` %                |
| Description    | Deegree on the color wheel.   | Intensity of the color.   | Brightness of the color.   |

!!! info "Disclaimer"
    Not all [terminals support](../../user-guide/compatibility/terminal-support.md) 24-bit colors in RGB, HSL, or Hex. If your terminal does support such advanced colors, read on.

<div class="color-cubes">
    <img src="../../../assets/images/cubes/cube_bright.svg" alt="Color cube bright">
    <img src="../../../assets/images/cubes/cube_dark.svg" alt="Color cube dark">
</div>

## Full Line Text Functions
You can output colors in HSL with the `hsl()` and `bg_hsl()` methods. The value for hue can be between `0`-`360` degrees, while saturation and lightness can be a percentage between `0`-`100` %:

Example:

```python linenums="1" hl_lines="3-4"
from colorist import hsl, bg_hsl

hsl("I want this text in green HSL colors", 120, 50, 50)
bg_hsl("I want this background in green HSL colors", 120, 50, 50)
```

How it appears in the terminal:

<pre><code>% <span style="color: hsl(120, 50%, 50%)">I want this text in green HSL colors</span>
% <span class="text-contrast" style="background-color: hsl(120, 50%, 50%)">I want this background in green HSL colors</span></code></pre>

## Custom String Styling
Or customize the styling of text and background with the `ColorHSL()` and `BgColorHSL()` classes:

```python linenums="1" hl_lines="6-7"
from colorist import ColorHSL, BgColorHSL

mustard_green = ColorHSL(60, 56, 43)
bg_steel_gray = BgColorHSL(190, 2, 49)

print(f"I want to use {mustard_green}MUSTARD GREEN{mustard_green.OFF}...")
print(f"... and {bg_steel_gray}STEEL GRAY{bg_steel_gray.OFF} colors")
```

How it appears in the terminal:

<pre><code>% I want to use <span style="color: hsl(60, 56%, 43%)">MUSTARD GREEN</span>...
% ... and <span class="text-contrast" style="background-color: hsl(190, 2%, 49%)">STEEL GRAY</span> colors</code></pre>
