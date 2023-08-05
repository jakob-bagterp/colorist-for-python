---
tags:
    - Features
    - Tutorial
---

# Text Effects and Other Styles
## Full Text Functions
In addition to colors, Colorist can also add effects when you print text in the terminal. How to print a full line of text with effects:

```python
from colorist import effect_blink

effect_blink("This is BLINKING!")
```

How it appears in the terminal:

![Example of terminal message with blinking text](../assets/images/examples/effect_full_text_blink_default.gif)

And this can also be combined with an optional color:

```python
from colorist import Color, effect_blink

effect_blink("This is BLINKING!", Color.CYAN)
```

How it appears in the terminal:

![Example of terminal message with blinking, cyan-colored text](../assets/images/examples/effect_full_text_blink_cyan.gif)

## Custom String Styling
How to customize terminal messages and change effect inside a paragraph:

```python
from colorist import Effect

print(f"I want {Effect.UNDERLINE}underlined text{Effect.UNDERLINE_OFF} inside this paragraph")

print(f"I want {Effect.BOLD}emphasized text{Effect.BOLD_OFF} inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with underline and bold text](../assets/images/examples/effect_custom_text_underline_bold.png)

## Mixing Effects and Colors
Effects can also be mixed with colors:

```python
from colorist import Color, Effect

print(f"I want both {Color.RED}colored and {Effect.BLINK}blinking{Effect.BLINK_OFF} text{Color.OFF} inside this paragraph")
```

How it appears in the terminal:

![Example of terminal message with red and blinking text](../assets/images/examples/effect_custom_text_blink_red.gif)

!!! tip
    Similar to `Color.OFF`, remember to turn off an effect with the relevant reset option (e.g `Effect.BOLD_OFF`, `Effect.DIM_OFF`, etc. or even just `Effect.OFF`) every time you want to revert back to the default terminal text style. Otherwise the effect may spill over and into other terminal messages.

## Overview
| Effect           | Full Text Function         | Custom             | Reset                  | Example    |
| ---------------- | -------------------------- | ------------------ | ---------------------- | ---------- |
| **Bold**         | `effect_bold("text")`      | `Effect.BOLD`      | `Effect.BOLD_OFF`      | ![Example of terminal message with bold text](../assets/images/examples/effect_map/bold_full_text_140x16.png) |
| Dim              | `effect_dim("text")`       | `Effect.DIM`       | `Effect.DIM_OFF`       | ![Example of terminal message with dimmed text](../assets/images/examples/effect_map/dim_full_text_140x16.png) |
| <u>Underline</u> | `effect_underline("text")` | `Effect.UNDERLINE` | `Effect.UNDERLINE_OFF` | ![Example of terminal message with underlined text](../assets/images/examples/effect_map/underline_full_text_140x16.png) |
| Blink            | `effect_blink("text")`     | `Effect.BLINK`     | `Effect.BLINK_OFF`     | ![Example of terminal message with blinking text](../assets/images/examples/effect_map/blink_full_text_140x16.gif) |
| Reverse          | `effect_reverse("text")`   | `Effect.REVERSE`   | `Effect.REVERSE_OFF`   | ![Example of terminal message with reversed text color and background](../assets/images/examples/effect_map/reverse_full_text_140x16.png) |
| Hide             | `effect_hide("text")`      | `Effect.HIDE`      | `Effect.HIDE_OFF`      | ![Example of terminal message with hidden text](../assets/images/examples/effect_map/hide_full_text_140x16.png) |
| -                | -                          | -                  | `Effect.OFF`           | -          |
