---
title: Print Text with Custom Effects and Styling
description: The easiest way to print text with custom effects and styling in terminal output using Colorist for Python. This documentation includes code examples.
tags:
    - Documentation
    - Tutorial
    - Effects
---

# Custom Text Effects and Styling
## `Effect`
Enumerable class of all available effects.

**Options:**

| Effect           | Effect Code        | Reset Code             | Example                                                                          |
| ---------------- | ------------------ | ---------------------- | -------------------------------------------------------------------------------- |
| Bold             | `Effect.BOLD`      | `Effect.BOLD_OFF`      | <code>This is <strong>BOLD</strong></code>                                       |
| Dim              | `Effect.DIM`       | `Effect.DIM_OFF`       | <code>This is <span class="effect-dimmed">DIMMED</span></code>                   |
| Underline        | `Effect.UNDERLINE` | `Effect.UNDERLINE_OFF` | <code>This is <u>UNDERLINED</u></code>                                           |
| Blink            | `Effect.BLINK`     | `Effect.BLINK_OFF`     | <code>This is <span class="effect-blinking">BLINKING</span></code>               |
| Reverse          | `Effect.REVERSE`   | `Effect.REVERSE_OFF`   | <code>This is <span class="bg-bright-white text-contrast">REVERSED</span></code> |
| Hide             | `Effect.HIDE`      | `Effect.HIDE_OFF`      | <code>This is <span class="effect-hidden">HIDDEN</span></code>                   |
| -                | -                  | `Effect.OFF`           | -                                                                                |

**Example:**

???+ example
    ```python linenums="1" hl_lines="3 5"
    from colorist import Effect

    print(f"I want {Effect.UNDERLINE}underlined text{Effect.UNDERLINE_OFF}")

    print(f"I want {Effect.BOLD}emphasized text{Effect.BOLD_OFF}")
    ```

    How it appears in the terminal:

    <pre><code>% I want <u>underlined text</u>
    % I want <strong>emphasized text</strong></code></pre>

!!! tip
    Similar to `Color.OFF`, remember to turn off an effect with the relevant reset option (e.g `Effect.BOLD_OFF`, `Effect.DIM_OFF`, etc. or even just `Effect.OFF`) every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.
