---
title: How to Add OKLCH Colors to Text
description: The easiest way to print colored text in terminal output using OKLCH and Colorist for Python. Includes code examples.
tags:
    - Features
    - Tutorial
    - Extended Colors
    - OKLCH Colors
---

# OKLCH Colors
## What Are OKLCH Colors?
The [OKLCH color model](https://oklch.net/) was created by Björn Ottosson in 2020 and has already been widely adopted by many browsers and applications after being standardized as CSS parameters a few years later. Unlike RGB, HSL, and many other color models, which are either linear or cylindrical, OKLCH takes a different approach.

Since humans perceive colors differently from how they are represented on screens as red, green, and blue — we actually see lightness, redness versus greenness, and blueness versus yellowness with our eye cones — OKLCH is designed to make colors appear more consistent to the human eye.

For example, when you change the hue in HSL, the perceived lightness of the color can vary significantly across the palette, making some colors appear much darker or lighter than others. In contrast, OKLCH maintains a consistent lightness across different hues, resulting in a uniform appearance.

### Example Gradients
OKLCH produces smoother and more visually appealing color transitions than HSL or RGB when transitioning from one color to another gradually. This is because the lightness component in OKLCH is designed to be perceptually uniform, leading to more natural-looking gradients.

For instance, consider the following comparison of gradients transitioning from red to blue using sRGB, HSL, and OKLCH:

<table id="color-model-gradients-table">
    <thead>
        <tr>
            <th>Model</th>
            <th>Gradient</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>sRGB</td>
            <td>
                <div class="gradient-wrapper">
                    <div class="gradient-srgb"></div>
                </div>
            </td>
            <td>This is slightly darker in the middle.</td>
        </tr>
        <tr>
            <td>HSL</td>
            <td>
                <div class="gradient-wrapper">
                    <div class="gradient-hsl"></div>
                </div>
            </td>
            <td>This is much brighter in the middle.</td>
        </tr>
        <tr>
            <td>OKLCH</td>
            <td>
                <div class="gradient-wrapper">
                    <div class="gradient-oklch"></div>
                </div>
            </td>
            <td>The brightness is more uniform throughout the color transition.</td>
        </tr>
    </tbody>
</table>

!!! info "Disclaimer"
    Not all [terminals support](../../user-guide/compatibility/terminal-support.md) 24-bit colors in RGB, HSL, Hex, or OKLCH. If your terminal does support such advanced colors, read on.

## Input Parameters
Each color in OKLCH can be defined as lightness, chroma, and hue:

| Parameter      | Lightness                | Chroma                  | Hue                        |
| -------------- | :----------------------: | :---------------------: | :------------------------: |
| Allowed values | `0.0`-`1.0`              | `0.0`-`0.4`             | `0`-`360` degrees          |
| Description    | Brightness of the color. | Intensity of the color. | Degree on the color wheel. |

### What Is Lightness?
Lightness is the brightness of the color. It ranges from `0.0` to `1.0`, where `0.0` is black and `1.0` is white. Example:

<table>
    <tbody>
        <tr>
            <td>Example</td>
            <td class="oklch-lightness-0-0"></td>
            <td class="oklch-lightness-0-1"></td>
            <td class="oklch-lightness-0-2"></td>
            <td class="oklch-lightness-0-3"></td>
            <td class="oklch-lightness-0-4"></td>
            <td class="oklch-lightness-0-5"></td>
            <td class="oklch-lightness-0-6"></td>
            <td class="oklch-lightness-0-7"></td>
            <td class="oklch-lightness-0-8"></td>
            <td class="oklch-lightness-0-9"></td>
            <td class="oklch-lightness-0-10"></td>
        </tr>
        <tr>
            <td>Lightness</td>
            <td>0.0</td>
            <td>0.1</td>
            <td>0.2</td>
            <td>0.3</td>
            <td>0.4</td>
            <td>0.5</td>
            <td>0.6</td>
            <td>0.7</td>
            <td>0.8</td>
            <td>0.9</td>
            <td>1.0</td>
        </tr>
    </tbody>
</table>

### What Is Hue?
Hue is the color wheel position from `0` to `360` degrees. Example:

<table>
    <tbody>
        <tr>
            <td>Example</td>
            <td class="oklch-hue-0"></td>
            <td class="oklch-hue-45"></td>
            <td class="oklch-hue-90"></td>
            <td class="oklch-hue-135"></td>
            <td class="oklch-hue-180"></td>
            <td class="oklch-hue-225"></td>
            <td class="oklch-hue-270"></td>
            <td class="oklch-hue-315"></td>
            <td class="oklch-hue-360"></td>
        </tr>
        <tr>
            <td>Hue</td>
            <td>0</td>
            <td>45</td>
            <td>90</td>
            <td>135</td>
            <td>180</td>
            <td>225</td>
            <td>270</td>
            <td>315</td>
            <td>360</td>
        </tr>
    </tbody>
</table>

### What Is Chroma?
While lightness and hue are relatively straightforward, chroma can be more difficult to understand. It represents the intensity or purity of a color. Higher values indicate more vivid, saturated colors, while lower values indicate more muted or grayish, unsaturated colors.

However, the maximum chroma value varies depending on the lightness and hue. Therefore, not all combinations of lightness, chroma, and hue produce valid colors.

Example:

<table>
    <tbody>
        <tr>
            <td>Example</td>
            <td class="oklch-chroma-0-00"></td>
            <td class="oklch-chroma-0-05"></td>
            <td class="oklch-chroma-0-10"></td>
            <td class="oklch-chroma-0-15"></td>
            <td class="oklch-chroma-0-20"></td>
            <td class="oklch-chroma-0-25"></td>
            <td class="oklch-chroma-0-30"></td>
            <td class="oklch-chroma-0-35"></td>
            <td class="oklch-chroma-0-40"></td>
        </tr>
        <tr>
            <td>Chroma</td>
            <td>0.00</td>
            <td>0.05</td>
            <td>0.10</td>
            <td>0.15</td>
            <td>0.20</td>
            <td>0.25</td>
            <td>0.30</td>
            <td>0.35</td>
            <td>0.40</td>
        </tr>
    </tbody>
</table>

Although the maximum chroma value of `0.4` can technically be higher and replicable on some wide-gamut displays, `0.4` is a reasonable limit for most use cases, as defined in the [CSS specification for `oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch).

### Converting OKLCH to RGB
Since the color spaces of OKLCH and RGB are different, it's not straightforward to convert between them. Here's a cheat sheet for converting OKLCH to pure red, green, and blue in RGB and Hex:

<div id="oklch-to-rgb-conversion-table"></div>

| Color   | Red                         | Green                        | Blue                         |
| ------- | :-------------------------: | :--------------------------: | :--------------------------: |
| Example |                             |                              |                              |
| OKLCH   | `oklch(0.628 0.2577 29.23)` | `oklch(0.8664 0.2948 142.5)` | `oklch(0.452 0.3132 264.05)` |
| RGB     | `rgb(255 0 0)`              | `rgb(0 255 0)`               | `rgb(0 0 255)`.              |
| Hex.    | `#ff0000`                   | `#00ff00`                    | `#0000ff`                    |

Find more conversions in the [official documentation for OKLCH](https://oklch.net/).

## Full Line Text Functions
Try the [`oklch()`](../../reference/extended-colors/oklch.md#colorist.print.foreground.oklch.MkDocstringsWrapper.oklch) and [`bg_oklch()`](../../reference/extended-colors/oklch.md#colorist.print.background.oklch.MkDocstringsWrapper.bg_oklch) methods for a full line of colored text..

Example:

```python linenums="1" hl_lines="3-4"
from colorist import oklch, bg_oklch

oklch("I want this text in orange OKLCH colors", 0.71, 0.1, 31)
bg_oklch("I want this background in orange OKLCH colors", 0.71, 0.1, 31)
```

How it appears in the terminal:

<pre><code>% <span style="color: oklch(0.71 0.1 31)">I want this text in orange OKLCH colors</span>
% <span class="text-contrast" style="background-color: oklch(0.71 0.1 31)">I want this background in orange OKLCH colors</span></code></pre>

## Custom String Styling
Or customize the styling of text and background with the [`ColorOKLCH()`](../../reference/extended-colors/oklch.md#coloroklchlightness-chroma-hue) and [`BgColorOKLCH()`](../../reference/extended-colors/oklch.md#bgcoloroklchlightness-chroma-hue) classes:

```python linenums="1" hl_lines="6-7"
from colorist import ColorOKLCH, BgColorOKLCH

neon_pink = ColorOKLCH(0.7, 0.3, 332)
bg_basil_green = BgColorOKLCH(0.54, 0.15, 141)

print(f"I want to use {neon_pink}NEON PINK{neon_pink.OFF}...")
print(f"... and {bg_basil_green}BASIL GREEN{bg_basil_green.OFF} colors")
```

How it appears in the terminal:

<pre><code>% I want to use <span style="color: oklch(0.7 0.3 332)">NEON PINK</span>...
% ... and <span class="text-contrast" style="background-color: oklch(0.54 0.15 141)">BASIL GREEN</span> colors</code></pre>
