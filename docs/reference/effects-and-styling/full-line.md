---
title: Print Text with Effects and Styling
description: The easiest way to print text with effects and styling in terminal output using Colorist for Python. This documentation includes code examples.
tags:
    - Documentation
    - Tutorial
    - Effects
---

# Full Line Text Functions for Effects and Styling
## Examples

| Effect           | Full Text Function         | Example                                                                          |
| ---------------- | -------------------------- | -------------------------------------------------------------------------------- |
| Bold             | `effect_bold("text")`      | <code>This is <strong>BOLD</strong></code>                                       |
| Dim              | `effect_dim("text")`       | <code>This is <span class="effect-dimmed">DIMMED</span></code>                   |
| Underline        | `effect_underline("text")` | <code>This is <u>UNDERLINED</u></code>                                           |
| Blink            | `effect_blink("text")`     | <code>This is <span class="effect-blinking">BLINKING</span></code>               |
| Reverse          | `effect_reverse("text")`   | <code>This is <span class="bg-bright-white text-contrast">REVERSED</span></code> |
| Hide             | `effect_hide("text")`      | <code>This is <span class="effect-hidden">HIDDEN</span></code>                   |

## Functions
::: colorist.print.effect.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true
