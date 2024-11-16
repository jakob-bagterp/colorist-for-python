---
title: How to Use Effects in ANSI Escape Codes
description: Learn how to use ANSI escape codes for text effects and styling like bold, underline, blink, dim, etc. in terminal output with Python. Includes code examples.
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
    - Effects
---

# Effects in ANSI Escape Codes
## Structure
For effects, the codes are. And as before, replace the two underscores `__` in `\x1b[__m` with any of the following color codes:

| Effect    | On  | Escape Code | Off | Escape Code | Output Example |
| :-------: | :-: | :---------: | :-: | :---------: | :------------- |
| Bold      | 1   | `\x1b[1m`   | 21  | `\x1b[21m`  | <code>This is <strong>BOLD</strong></code> |
| Dim       | 2   | `\x1b[2m`   | 22  | `\x1b[22m`  | <code>This is <span class="effect-dimmed">DIMMED</span></code> |
| Underline | 4   | `\x1b[4m`   | 24  | `\x1b[24m`  | <code>This is <u>UNDERLINED</u></code> |
| Blink     | 5   | `\x1b[5m`   | 25  | `\x1b[25m`  | <code>This is <span class="effect-blinking">BLINKING</span></code> |
| Reverse   | 7   | `\x1b[7m`   | 27  | `\x1b[27m`  | <code>This is <span class="bg-bright-white">REVERSED</span></code> |
| Hide      | 8   | `\x1b[7m`   | 28  | `\x1b[28m`  | <code>This is <span class="effect-hidden">HIDDEN</span></code> |

!!! info "Different Color Schemes in Different Terminals"
    Most terminals apply different color schemes so `\x1b[31m` or `Color.RED` won't produce the exact same screen color of red. Some straight, others with an orange tint. For further reading, refer to this [list of common terminals and their color schemes](https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit).

## Examples
For example, `\x1b[4m` is underlined text, and `\x1b[24m` turns off the underline effect. When wrapped in a print statement, you can write this:

```python
print("This is \x1b[1mUNDERLINED\x1b[21m text")
```

How it looks in the terminal:

<pre><code>% This is <u>UNDERLINED</u> text</code></pre>

Another example with blinking text:

```python
print("This is \x1b[5mBLINKING\x1b[25m text")
```

How it looks in the terminal:

<pre><code>% This is <span class="effect-blinking">BLINKING</span> text</code></pre>
