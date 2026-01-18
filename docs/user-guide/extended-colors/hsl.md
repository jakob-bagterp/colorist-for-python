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
## What Are HSL Colors?
The 24-bit HSL color space covers over 16 million colors, and each color can be defined by three parameters:

* Hue
* Saturation
* Lightness

The model represents color as a cylindrical coordinate system rather than a set of primary color intensities like RGB. It was designed to be more intuitive for humans, as it allows you to change the shade or intensity of a color by adjusting a single numerical value rather than recalculating three different color channels.

!!! info "Disclaimer"
    Not all [terminals support](../../user-guide/compatibility/terminal-support.md) 24-bit colors in RGB, HSL, Hex, or OKLCH. If your terminal does support such advanced colors, read on.

## Input Parameters
Each color in HSL is defined as hue, saturation, and lightness with the following allowed values:

| Parameter      | Hue                        | Saturation              | Lightness                |
| -------------- | :------------------------: | :---------------------: | :----------------------: |
| Allowed values | `0`-`360` degrees          | `0`-`100` %             | `0`-`100` %              |
| Description    | Degree on the color wheel. | Intensity of the color. | Brightness of the color. |

### What Is Hue?
Hue represents the color wheel position from `0` to `360` degrees. Simply by changing this value, you can easily cover the entire color spectrum:

<div class="gradient-wrapper">
    <div class="gradient-hsl-full-color-wheel"></div>
</div>

### What Is Saturation?
Saturation represents the intensity or purity of a color. Higher values indicate more vivid, saturated colors, while lower values indicate more muted or grayish, unsaturated colors. Example:

<table>
    <tbody>
        <tr>
            <td>Example</td>
            <td class="hsl-saturation-0"></td>
            <td class="hsl-saturation-10"></td>
            <td class="hsl-saturation-20"></td>
            <td class="hsl-saturation-30"></td>
            <td class="hsl-saturation-40"></td>
            <td class="hsl-saturation-50"></td>
            <td class="hsl-saturation-60"></td>
            <td class="hsl-saturation-70"></td>
            <td class="hsl-saturation-80"></td>
            <td class="hsl-saturation-90"></td>
            <td class="hsl-saturation-100"></td>
        </tr>
        <tr>
            <td>Saturation</td>
            <td>0</td>
            <td>10</td>
            <td>20</td>
            <td>30</td>
            <td>40</td>
            <td>50</td>
            <td>60</td>
            <td>70</td>
            <td>80</td>
            <td>90</td>
            <td>100</td>
        </tr>
    </tbody>
</table>

### What Is Lightness?
Lightness represents the brightness of the color. It ranges from `0` to `100` %, where `0` % is black and `100` % is white. Example:

<table>
    <tbody>
        <tr>
            <td>Example</td>
            <td class="hsl-lightness-0"></td>
            <td class="hsl-lightness-10"></td>
            <td class="hsl-lightness-20"></td>
            <td class="hsl-lightness-30"></td>
            <td class="hsl-lightness-40"></td>
            <td class="hsl-lightness-50"></td>
            <td class="hsl-lightness-60"></td>
            <td class="hsl-lightness-70"></td>
            <td class="hsl-lightness-80"></td>
            <td class="hsl-lightness-90"></td>
            <td class="hsl-lightness-100"></td>
        </tr>
        <tr>
            <td>Lightness</td>
            <td>0</td>
            <td>10</td>
            <td>20</td>
            <td>30</td>
            <td>40</td>
            <td>50</td>
            <td>60</td>
            <td>70</td>
            <td>80</td>
            <td>90</td>
            <td>100</td>
        </tr>
    </tbody>
</table>

## Full Line Text Functions
You can output colors in HSL with the [`hsl()`](../../reference/extended-colors/hsl.md#colorist.print.foreground.hsl.MkDocstringsWrapper.hsl) and [`bg_hsl()`](../../reference/extended-colors/hsl.md#colorist.print.background.hsl.MkDocstringsWrapper.bg_hsl) methods. The value for hue can be between `0`-`360` degrees, while saturation and lightness can be a percentage between `0`-`100` %:

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
Or customize the styling of text and background with the [`ColorHSL()`](../../reference/extended-colors/hsl.md#colorhslhue-saturation-lightness) and [`BgColorHSL()`](../../reference/extended-colors/hsl.md#bgcolorhslhue-saturation-lightness) classes:

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
