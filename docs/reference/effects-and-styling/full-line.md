---
tags:
    - Documentation
    - Tutorial
---

# Full Text Functions for Text Effects and Styling
## Examples

| Effect           | Full Text Function         | Example |
| ---------------- | -------------------------- | ------- |
| Bold             | `effect_bold("text")`      | <code>This is <strong>BOLD</strong></code> |
| Dim              | `effect_dim("text")`       | ![Example of terminal message with dimmed text](../../assets/images/examples/effect_map/dim_full_text_140x16.png) |
| Underline        | `effect_underline("text")` | <code>This is <u>UNDERLINED</u></code> |
| Blink            | `effect_blink("text")`     | ![Example of terminal message with blinking text](../../assets/images/examples/effect_map/blink_full_text_140x16.gif) |
| Reverse          | `effect_reverse("text")`   | ![Example of terminal message with reversed text color and background](../../assets/images/examples/effect_map/reverse_full_text_140x16.png) |
| Hide             | `effect_hide("text")`      | ![Example of terminal message with hidden text](../../assets/images/examples/effect_map/hide_full_text_140x16.png) |

## Functions
::: colorist.print.effect.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true