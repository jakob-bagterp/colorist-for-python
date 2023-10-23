---
tags:
    - Features
    - Tutorial
---

# RGB Colors
!!! info "Disclaimer"
    Not all [terminals support](../materials/terminal-support.md) RGB, HSL, or Hex colors. If your terminal does support such advanced colors, read on.

## Full Text Functions
Try the `rgb()` and `bg_rgb()` methods for a full line of colored text. The values for red, green, blue can be an integer between `0-255`.

Example:

```python
from colorist import rgb, bg_rgb

rgb("I want this text in blue RGB colors", 0, 128, 255)
bg_rgb("I want this background in blue RGB colors", 0, 128, 255)
```

How it appears in the terminal:

<pre><code>% <span style="color: rgb(0, 128, 255)">I want this text in blue RGB colors</span>
% <span style="background-color: rgb(0, 128, 255)">I want this background in blue RGB colors</span></code></pre>

## Custom String Styling
Or customize the styling of text and background with the `ColorRGB()` and `BgColorRGB()` classes:

```python
from colorist import ColorRGB, BgColorRGB

dusty_pink = ColorRGB(194, 145, 164)
bg_steel_blue = BgColorRGB(70, 130, 180)

print(f"I want to use {dusty_pink}dusty pink{dusty_pink.OFF}...")
print(f"... {bg_steel_blue}steel blue{bg_steel_blue.OFF} colors")
```

How it appears in the terminal:

<pre><code>% I want to use <span style="color: rgb(194, 145, 164)">dusty pink</span>...
% ... <span style="background-color: rgb(70, 130, 180)">steel blue</span> colors</code></pre>
