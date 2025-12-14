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
For effects and text styling, the escape codes are similar to the [standard colors](standard-16-colors.md).

For example, the sequence `\x1b[4m` for underlined styling can be broken down into the following parts:

| Part        | `\x1b[` | `4` | `m` |
| ----------- | :-----: | :-: | :-: |
| Description | Starts sequence, also called the Control Sequence Introducer (CSI). | Effect on or off, respectively between `1`-`8` or `21`-`28`. | Ends sequence and calls the graphics function Select Graphic Rendition (SGR). |

## Cheat Sheet

| Effect    | On  | Escape Code | Off | Escape Code | Output Example                                                                   |
| :-------: | :-: | :---------: | :-: | :---------: | :------------------------------------------------------------------------------- |
| Bold      | 1   | `\x1b[1m`   | 21  | `\x1b[21m`  | <code>This is <strong>BOLD</strong></code>                                       |
| Dim       | 2   | `\x1b[2m`   | 22  | `\x1b[22m`  | <code>This is <span class="effect-dimmed">DIMMED</span></code>                   |
| Underline | 4   | `\x1b[4m`   | 24  | `\x1b[24m`  | <code>This is <u>UNDERLINED</u></code>                                           |
| Blink     | 5   | `\x1b[5m`   | 25  | `\x1b[25m`  | <code>This is <span class="effect-blinking">BLINKING</span></code>               |
| Reverse   | 7   | `\x1b[7m`   | 27  | `\x1b[27m`  | <code>This is <span class="bg-bright-white text-contrast">REVERSED</span></code> |
| Hide      | 8   | `\x1b[7m`   | 28  | `\x1b[28m`  | <code>This is <span class="effect-hidden">HIDDEN</span></code>                   |

!!! info "Different Color Schemes in Different Terminals"
    Most terminals apply different color schemes so `\x1b[31m` or `Color.RED` won't produce the exact same screen color of red. Some straight, others with an orange tint. For further reading, refer to this [list of common terminals and their color schemes](https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit).

## Examples
For example, `\x1b[4m` is underlined text, and `\x1b[24m` turns off the underline effect. When wrapped in a print statement, you can write this:

```python
print("This is \x1b[1mUNDERLINED\x1b[21m text")
```

How it appears in the terminal:

<pre><code>% This is <u>UNDERLINED</u> text</code></pre>

Another example with blinking text:

```python
print("This is \x1b[5mBLINKING\x1b[25m text")
```

How it appears in the terminal:

<pre><code>% This is <span class="effect-blinking">BLINKING</span> text</code></pre>

!!! tip "How to Use Effects with Colorist"
    Instead of using raw ANSI escape codes, it's [convenient to use Colorist](../user-guide/index.md) to generate them while keeping the code readable.

    Simply use the `Effect` class for [effects and styling](../user-guide/effects-and-styling.md). For example:

    ```python linenums="1" hl_lines="3-4"
    from colorist import Effect

    print(f"This is {Effect.UNDERLINE}UNDERLINED{Effect.OFF} text")
    print(f"This is {Effect.BLINK}BLINKING{Effect.BLINK} text")
    ```

    How it appears in the terminal:

    <pre><code>% This is <u>UNDERLINED</u> text
    % This is <span class="effect-blinking">BLINKING</span> text</code></pre>

## Support the Project
If you have already downloaded and tried the package – maybe even used it in a production environment – perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution makes a difference, whether you buy a coffee or support with a monthly donation. Find your tier here:

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
