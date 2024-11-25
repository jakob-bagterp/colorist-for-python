---
title: How to Use RGB Colors in ANSI Escape Codes
description: Learn how to use 24-bit RGB colors in terminal output using Python and ANSI escape codes. Includes code examples.
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
    - RGB Colors
---

# 24-Bit RGB Colors in ANSI Escape Codes
## Structure
The 24-bit RGB color space represents a much broader array of colors. Simply use any number from `0` to `255` to set each of the red `r`, green `g`, and blue `b` colors in the sequences `38;2;r;g;b` for text color and `38;2;r;g;b` for background color:

| Code               | Placement  |
| :----------------: | :--------: |
| `\x1b[38;2;r;g;bm` | Text       |
| `\x1b[48;2;r;g;bm` | Background |

### Sequence Parts
For example, the color code for light blue `rgb(173, 216, 230)` can be broken down into the following parts:

| Part        | `\x1b[` | `38;2;`<br>`48;2;` | `173;216;230` | `m` |
| ----------- | :-----: | :----------------: | :-----------: | :-: |
| Description | Starts sequence, also called the Control Sequence Introducer (CSI). | Select foreground text or background color. | RGB color code where each number is between 0-255. | Ends sequence and calls the graphics function Select Graphic Rendition (SGR). |

!!! info "Disclaimer"
    Not all [terminals support](../user-guide/materials/terminal-support.md) 24-bit colors in RGB, HSL, or Hex. If your terminal does support such advanced colors, read on.

## Examples
For example, `\x1b[38;2;142;194;21m` is a lime green foreground text color, and `\x1b[48;2;194;21;139m` is a rosa background color. When wrapped with `\x1b[0m` to reset the color, you can write this:

```python linenums="1"
print("This is \x1b[38;2;142;194;21mLIME GREEN\x1b[0m text")
print("This is \x1b[48;2;194;21;139mROSA\x1b[0m background")
```

How it appears in the terminal:

<pre><code>% This is <span style="color: #8ec215;">LIME GREEN</span> text
% This is <span class="text-contrast" style="background-color: #c2158b;">ROSA</span> background</code></pre>

!!! tip "How to Use RGB Colors with Colorist"
    Instead of using raw ANSI escape codes, it's [convenient to use Colorist](../user-guide/index.md) to generate them while keeping the code readable.

    Simply use the `ColorRGB` class for [foreground text colors](../user-guide/extended-colors/rgb.md) or the `BgColorRGB` class for [background colors](../user-guide/extended-colors/rgb.md). For example:

    ```python linenums="1" hl_lines="3-4"
    from colorist import ColorRGB, BgColorRGB

    lime_green = ColorRGB(142, 194, 21)
    rosa = BgColorRGB(194, 21, 139)

    print(f"This is {lime_green}LIME GREEN{lime_green.OFF} text")
    print(f"This is {rosa}ROSA{rosa.OFF} background")
    ```

    How it appears in the terminal:

    <pre><code>% This is <span style="color: #8ec215;">LIME GREEN</span> text
    % This is <span class="text-contrast" style="background-color: #c2158b;">ROSA</span> background</code></pre>

    In Colorist, the [RGB color space](../user-guide/extended-colors/rgb.md) is used to furthermore support definition of colors as [HSL](../user-guide/extended-colors/hsl.md) or [Hex](../user-guide/extended-colors/hex.md).
