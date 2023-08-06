---
tags:
    - Documentation
    - Tutorial
---

# Text Effects and Styling
## Full Text Functions

::: colorist.print.effect.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 4
      merge_init_into_class: true

### Examples
| Effect           | Full Text Function         | Example |
| ---------------- | -------------------------- | ------- |
| **Bold**         | `effect_bold("text")`      | ![Example of terminal message with bold text](../assets/images/examples/effect_map/bold_full_text_140x16.png) |
| Dim              | `effect_dim("text")`       | ![Example of terminal message with dimmed text](../assets/images/examples/effect_map/dim_full_text_140x16.png) |
| <u>Underline</u> | `effect_underline("text")` | ![Example of terminal message with underlined text](../assets/images/examples/effect_map/underline_full_text_140x16.png) |
| Blink            | `effect_blink("text")`     | ![Example of terminal message with blinking text](../assets/images/examples/effect_map/blink_full_text_140x16.gif) |
| Reverse          | `effect_reverse("text")`   | ![Example of terminal message with reversed text color and background](../assets/images/examples/effect_map/reverse_full_text_140x16.png) |
| Hide             | `effect_hide("text")`      | ![Example of terminal message with hidden text](../assets/images/examples/effect_map/hide_full_text_140x16.png) |

## Custom String Styling
### `Effect`
Enumerable class of all available effects.

**Options:**

| Effect           | Custom             | Reset                  | Example    |
| ---------------- | ------------------ | ---------------------- | ---------- |
| **Bold**         | `Effect.BOLD`      | `Effect.BOLD_OFF`      | ![Example of terminal message with bold text](../assets/images/examples/effect_map/bold_full_text_140x16.png) |
| Dim              | `Effect.DIM`       | `Effect.DIM_OFF`       | ![Example of terminal message with dimmed text](../assets/images/examples/effect_map/dim_full_text_140x16.png) |
| <u>Underline</u> | `Effect.UNDERLINE` | `Effect.UNDERLINE_OFF` | ![Example of terminal message with underlined text](../assets/images/examples/effect_map/underline_full_text_140x16.png) |
| Blink            | `Effect.BLINK`     | `Effect.BLINK_OFF`     | ![Example of terminal message with blinking text](../assets/images/examples/effect_map/blink_full_text_140x16.gif) |
| Reverse          | `Effect.REVERSE`   | `Effect.REVERSE_OFF`   | ![Example of terminal message with reversed text color and background](../assets/images/examples/effect_map/reverse_full_text_140x16.png) |
| Hide             | `Effect.HIDE`      | `Effect.HIDE_OFF`      | ![Example of terminal message with hidden text](../assets/images/examples/effect_map/hide_full_text_140x16.png) |
| -                | -                  | `Effect.OFF`           | -          |

**Example:**

???+ example
    ```python linenums="1"
    from colorist import Effect

    print(f"I want {Effect.UNDERLINE}underlined text{Effect.UNDERLINE_OFF} inside this paragraph")

    print(f"I want {Effect.BOLD}emphasized text{Effect.BOLD_OFF} inside this paragraph")
    ```

    How it appears in the terminal:

    ![Example of terminal message with underline and bold text](../assets/images/examples/effect_custom_text_underline_bold.png)

!!! tip
    Similar to `Color.OFF`, remember to turn off an effect with the relevant reset option (e.g `Effect.BOLD_OFF`, `Effect.DIM_OFF`, etc. or even just `Effect.OFF`) every time you want to revert back to the default terminal text style. Otherwise the effect may spill over and into other terminal messages.
