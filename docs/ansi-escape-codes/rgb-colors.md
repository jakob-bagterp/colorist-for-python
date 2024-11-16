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

!!! info "Disclaimer"
    Not all [terminals support](../user-guide/materials/terminal-support.md) 24-bit colors in RGB, HSL, or Hex. If your terminal does support such advanced colors, read on.

## Examples
For example, `\x1b[38;2;142;194;21m` is a lime green foreground text color, and `\x1b[48;2;194,21,139m` is a rosa background color. When wrapped with `\x1b[0m` to reset the color, you can write this:

```python
print("This is \x1b[38;2;142;194;21mLIME GREEN\x1b[0m text")
print("This is \x1b[48;2;194,21,139mROSA\x1b[0m background")
```

How it looks in the terminal:

<pre><code>% This is <span class="extended-colors" style="--fg-color: #8ec215;">LIME GREEN</span> text
% This is <span class="extended-colors" style="--bg-color: #c2158b;">ROSA</span> background</code></pre>

## How to Use RGB Colors in Colorist
In Colorist, the [RGB color space](../user-guide/extended-colors/rgb.md) is used to furthermore support definition of colors as [HSL](../user-guide/extended-colors/hsl.md) or [Hex](../user-guide/extended-colors/hex.md).
