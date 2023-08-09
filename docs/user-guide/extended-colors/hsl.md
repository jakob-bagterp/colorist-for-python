---
tags:
    - Features
    - Tutorial
---

# HSL Colors
!!! info "Disclaimer"
    Not all [terminals support](../../user-guide/materials/terminal-support.md) RGB, HSL, or Hex colors. If your terminal does support such advanced colors, read on.

## Full Text Functions
You can output colors in HSL with the `hsl()` and `bg_hsl()` methods. The value for hue can be between `0-360` degrees, while saturation and lightness can be a percentage between `0-100` %:

```python
from colorist import hsl, bg_hsl

hsl("I want this text in green HSL colors", 120, 50, 50)
bg_hsl("I want this background in green HSL colors", 120, 50, 50)
```

How it appears in the terminal:

![Example of text in HSL colors printed in a terminal window](../../assets/images/examples/hsl_full_text.png)

## Custom String Styling
Or customize the styling of text and background with the `ColorHSL()` and `BgColorHSL()` classes:

```python
from colorist import ColorHSL, BgColorHSL

mustard_green = ColorHSL(60, 56, 43)
bg_steel_gray = BgColorHSL(190, 2, 49)

print(f"I want to use {mustard_green}mustard green{mustard_green.OFF} and {bg_steel_gray}steel blue{bg_steel_gray.OFF} colors inside this paragraph")
```

How it appears in the terminal:

![Another example of text in HSL colors printed in a terminal window](../../assets/images/examples/hsl_custom_text.png)
