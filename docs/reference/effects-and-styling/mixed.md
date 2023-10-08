---
tags:
    - Documentation
    - Tutorial
---

# Custom Text Effects and Styling
## `Effect`
Enumerable class of all available effects.

**Options:**

| Effect           | Custom             | Reset                  | Example    |
| ---------------- | ------------------ | ---------------------- | ---------- |
| Bold             | `Effect.BOLD`      | `Effect.BOLD_OFF`      | <code>This is <strong>BOLD</strong></code> |
| Dim              | `Effect.DIM`       | `Effect.DIM_OFF`       | ![Example of terminal message with dimmed text](../../assets/images/examples/effect_map/dim_full_text_140x16.png) |
| <u>Underline</u> | `Effect.UNDERLINE` | `Effect.UNDERLINE_OFF` | <code>This is <u>UNDERLINED</u></code> |
| Blink            | `Effect.BLINK`     | `Effect.BLINK_OFF`     | <code><span class="effect-blinking">This is BLINKING</span></code> |
| Reverse          | `Effect.REVERSE`   | `Effect.REVERSE_OFF`   | ![Example of terminal message with reversed text color and background](../../assets/images/examples/effect_map/reverse_full_text_140x16.png) |
| Hide             | `Effect.HIDE`      | `Effect.HIDE_OFF`      | ![Example of terminal message with hidden text](../../assets/images/examples/effect_map/hide_full_text_140x16.png) |
| -                | -                  | `Effect.OFF`           | -          |

**Example:**

???+ example
    ```python linenums="1"
    from colorist import Effect

    print(f"I want {Effect.UNDERLINE}underlined text{Effect.UNDERLINE_OFF}")

    print(f"I want {Effect.BOLD}emphasized text{Effect.BOLD_OFF}")
    ```

    How it appears in the terminal:

    <pre><code>% I want <u>underlined text</u>
    % I want <strong>emphasized text</strong></code></pre>

!!! tip
    Similar to `Color.OFF`, remember to turn off an effect with the relevant reset option (e.g `Effect.BOLD_OFF`, `Effect.DIM_OFF`, etc. or even just `Effect.OFF`) every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.
