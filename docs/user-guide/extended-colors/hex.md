---
tags:
    - Features
    - Tutorial
    - Extended Colors
    - Hex Colors
---

# Hex Colors
The 24-bit Hex color model covers over 16 million colors, and each color can be defined with a code in hexadecimal, for instance `#00aaff`, that can be broken down into a [RGB value](rgb.md):

| Hex Code | RGB Value | Color |
| -------- | --------- | ----- |
| `00`     | `0`       | Red   |
| `aa`     | `170`     | Green |
| `ff`     | `255`     | Blue  |

!!! info "Disclaimer"
    Not all [terminals support](../materials/terminal-support.md) 24-bit colors in RGB, HSL, or Hex. If your terminal does support such advanced colors, read on.

## Full Text Functions
Try the `hex()` and `bg_hex()` methods for a full line of colored text. Allowed Hex values are, for instance, `#00aaff` or `#0af`, alternatively without the hash sign as `00aaff` or `0af`.

Example:

```python
from colorist import hex, bg_hex

hex("I want this text in coral Hex colors", "#ff7f50")
bg_hex("I want this background in coral Hex colors", "#ff7f50")
```

How it appears in the terminal:

<pre><code>% <span style="color: #ff7f50">I want this text in coral Hex colors</span>
% <span style="background-color: #ff7f50">I want this background in coral Hex colors</span></code></pre>

## Custom String Styling
Or customize the styling of text and background with the `ColorHex()` and `BgColorHex()` classes:

```python
from colorist import ColorHex, BgColorHex

watermelon_red = ColorHex("#ff5733")
bg_mint_green = BgColorHex("#99ff99")

print(f"I want to use {watermelon_red}watermelon red{watermelon_red.OFF}...")
print(f"... and {bg_mint_green}mint green{bg_mint_green.OFF} colors")
```

How it appears in the terminal:

<pre><code>% I want to use <span style="color: #ff5733">watermelon red</span>...
% ... <span style="background-color: #99ff99">mint green</span> colors</code></pre>
