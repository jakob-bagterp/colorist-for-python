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
| Dim              | `effect_dim("text")`       | <code><span class="effect-dimmed">This is DIMMED</span></code> |
| Underline        | `effect_underline("text")` | <code>This is <u>UNDERLINED</u></code> |
| Blink            | `effect_blink("text")`     | <code><span class="effect-blinking">This is BLINKING</span></code> |
| Reverse          | `effect_reverse("text")`   | <code><span class="bg-bright-white">This is REVERSED</span></code> |
| Hide             | `effect_hide("text")`      | ![Example of terminal message with hidden text](../../assets/images/examples/effect_map/hide_full_text_140x16.png) |

## Functions
::: colorist.print.effect.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true
