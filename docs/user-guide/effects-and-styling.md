---
title: How to Add Effects and Styling to Text
description: The easiest way to add effects and text styling to terminal output using Colorist for Python. Includes code examples.
tags:
    - Features
    - Tutorial
    - Effects
---

# How to Add Effects and Styling to Text
## Full Text Functions
### Examples
In addition to colors, Colorist can also add effects when you print text in the terminal. How to print a full line of text with effects:

```python linenums="1" hl_lines="3"
from colorist import effect_blink

effect_blink("This is BLINKING!")
```

How it appears in the terminal:

<pre><code>% <span class="effect-blinking">This is BLINKING!</span></code></pre>

### Mixing Effects and Colors
This can also be combined with an optional color:

```python linenums="1" hl_lines="3"
from colorist import Color, effect_blink

effect_blink("CYAN and BLINKING!", Color.CYAN)
```

How it appears in the terminal:

<pre><code>% <span class="effect-blinking fg-cyan">CYAN and BLINKING!</span></code></pre>

### Cheat Sheet

| Effect           | Full Text Function         | Example                                                            |
| ---------------- | -------------------------- | ------------------------------------------------------------------ |
| Bold             | `effect_bold("text")`      | <code>This is <strong>BOLD</strong></code>                         |
| Dim              | `effect_dim("text")`       | <code>This is <span class="effect-dimmed">DIMMED</span></code>     |
| Underline        | `effect_underline("text")` | <code>This is <u>UNDERLINED</u></code>                             |
| Blink            | `effect_blink("text")`     | <code>This is <span class="effect-blinking">BLINKING</span></code> |
| Reverse          | `effect_reverse("text")`   | <code>This is <span class="bg-bright-white">REVERSED</span></code> |
| Hide             | `effect_hide("text")`      | <code>This is <span class="effect-hidden">HIDDEN</span></code>     |

## Custom String Styling
### Examples
How to customize terminal messages and change effect inside a paragraph:

```python linenums="1" hl_lines="3 5"
from colorist import Effect

print(f"I want {Effect.UNDERLINE}underlined text{Effect.UNDERLINE_OFF}")

print(f"I want {Effect.BOLD}emphasized text{Effect.BOLD_OFF}")
```

How it appears in the terminal:

<pre><code>% I want <u>underlined text</u>
% I want <strong>emphasized text</strong></code></pre>

### Mixing Effects and Colors
Effects can also be mixed with colors:

```python linenums="1" hl_lines="3"
from colorist import Color, Effect

print(f"I want both {Color.RED}colored and {Effect.BLINK}blinking{Effect.BLINK_OFF} text{Color.OFF} inside this paragraph")
```

How it appears in the terminal:

<pre><code>% I want both <span class="fg-red">colored and <span class="effect-blinking">blinking</span> text</span> inside this paragraph</code></pre>

!!! tip
    Similar to `Color.OFF`, remember to turn off an effect with the relevant reset option (e.g `Effect.BOLD_OFF`, `Effect.DIM_OFF`, etc. or even just `Effect.OFF`) every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

### Cheat Sheet

| Effect           | Reset Code         | Reset Code             | Example                                                            |
| ---------------- | ------------------ | ---------------------- | ------------------------------------------------------------------ |
| Bold             | `Effect.BOLD`      | `Effect.BOLD_OFF`      | <code>This is <strong>BOLD</strong></code>                         |
| Dim              | `Effect.DIM`       | `Effect.DIM_OFF`       | <code>This is <span class="effect-dimmed">DIMMED</span></code>     |
| Underline        | `Effect.UNDERLINE` | `Effect.UNDERLINE_OFF` | <code>This is <u>UNDERLINED</u></code>                             |
| Blink            | `Effect.BLINK`     | `Effect.BLINK_OFF`     | <code>This is <span class="effect-blinking">BLINKING</span></code> |
| Reverse          | `Effect.REVERSE`   | `Effect.REVERSE_OFF`   | <code>This is <span class="bg-bright-white">REVERSED</span></code> |
| Hide             | `Effect.HIDE`      | `Effect.HIDE_OFF`      | <code>This is <span class="effect-hidden">HIDDEN</span></code>     |
| -                | -                  | `Effect.OFF`           | -                                                                  |
