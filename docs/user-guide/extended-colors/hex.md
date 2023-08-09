---
tags:
    - Features
    - Tutorial
---

# Hex Colors
!!! info "Disclaimer"
    Not all [terminals support](../materials/terminal-support.md) RGB, HSL, or Hex colors. If your terminal does support such advanced colors, read on.

## Full Text Functions
Try the `hex()` and `bg_hex()` methods for a full line of colored text. Allowed Hex values are, for instance, `#00aaff` or `#0af`, alternatively without the hash sign as `00aaff` or `0af`.

```python
from colorist import hex, bg_hex

hex("I want this text in coral Hex colors", "#ff7f50")
bg_hex("I want this background in coral Hex colors", "#ff7f50")
```

How it appears in the terminal:

![Example of text in Hex colors printed in a terminal window](../../assets/images/examples/hex_full_text.png)

## Custom String Styling
Or customize the styling of text and background with the `ColorHex()` and `BgColorHex()` classes:

```python
from colorist import ColorHex, BgColorHex

watermelon_red = ColorHex("#ff5733")
bg_mint_green = BgColorHex("#99ff99")

print(f"I want to use {watermelon_red}watermelon pink{watermelon_red.OFF} and {bg_mint_green}mint green{bg_mint_green.OFF} colors inside this paragraph")
```

How it appears in the terminal:

![Another example of text in Hex colors printed in a terminal window](../../assets/images/examples/hex_custom_text.png)
