---
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
    - Effects
---

# Effects in ANSI Escape Codes
For effects, the codes are. And as before, replace the two underscores `__` in `\x1b[__m` with any of the following color codes:

| Effect    | On  | Off | Example |
| :-------: | :-: | :-: | :-----: |
| Bold      | 1   | 21  | <code>This is <strong>BOLD</strong></code> |
| Dim       | 2   | 22  | <code>This is <span class="effect-dimmed">DIMMED</span></code> |
| Underline | 4   | 24  | <code>This is <u>UNDERLINED</u></code> |
| Blink     | 5   | 25  | <code>This is <span class="effect-blinking">BLINKING</span></code> |
| Reverse   | 7   | 27  | <code>This is <span class="bg-bright-white">REVERSED</span></code> |
| Hide      | 8   | 28  | <code>This is <span class="effect-hidden">HIDDEN</span></code> |

!!! info "Different Color Schemes in Different Terminals"
    Most terminals apply different color schemes so `\x1b[31m` or `Color.RED` won't produce the exact same screen color of red. Some straight, others with an orange tint. For further reading, refer to this [list of common terminals and their color schemes](https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit).
