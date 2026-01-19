---
title: How to Customize Text with ANSI Escape Codes
description: Learn how to apply custom colors, effects and styling to text and background, even without knowing ANSI escape codes. Includes code examples.
tags:
    - Tutorial
    - Text Colors
    - Foreground Colors
    - Background Colors
    - Standard Colors
    - Extended Colors
    - Hex Colors
    - HSL Colors
    - RGB Colors
    - VGA Colors
    - OKLCH Colors
    - Effects
---

# How to Customize Text Styling and Colors with ANSI Escape Codes
Instead of printing statements directly to the terminal, you can also customize and combine various colors and styling to text strings before printing them. This gives you more flexibility to create complex patterns with different styles.

## How It Works
When using the [`style_text()`](../../reference/custom/text-styling.md#colorist.style.text.MkDocstringsWrapper.style_text) method to apply colors and styling to a text string...

```python linenums="1" hl_lines="3"
from colorist import style_text, Color

text = style_text("APPROVED", Color.GREEN)
```

... this then wraps the text in the relevant [ANSI escape codes](../../ansi-escape-codes/introduction.md), e.g. `\033[32mAPPROVED\033[0m`.

If you print the newly styled text...

```python linenums="4" title=""
print(text)
```

... it appears like this in the terminal:

<pre><code>% <span class="fg-green">APPROVED</span></code></pre>

## Examples
### Single Style
In addition to standard colors for [text](../standard-colors/text-foreground.md) and [background](../standard-colors/background.md), you can also use [effects](../effects-and-styling.md) as well as extended colors for the [VGA](../extended-colors/vga.md), [RGB](../extended-colors/rgb.md), [HSL](../extended-colors/hsl.md), [Hex](../extended-colors/hex.md), and [OKLCH](../extended-colors/oklch.md) palettes.

For example:

```python linenums="1" hl_lines="3"
from colorist import style_text, BgColorRGB

text = style_text("I want BURGUNDY background", BgColorRGB(128, 0, 32))
print(text)
```

How it appears in the terminal:

<pre><code>% <span class="text-contrast" style="background-color: rgb(128, 0, 32)">I want BURGUNDY background</span></code></pre>

!!! info "Disclaimer"
    Not all [terminals support](../../user-guide/compatibility/terminal-support.md) 8-bit VGA colors or 24-bit colors in RGB, HSL, Hex, or OKLCH. If your terminal does support such advanced colors, read on.

### Multiple Styles
You can also combine several styles by adding multiple styling arguments to the `style_text()` method:

```python linenums="1" hl_lines="3"
from colorist import style_text, Color, Effect

warning = style_text("WARNING", Color.YELLOW, Effect.BOLD, Effect.BLINK)
print(warning)
```

How it appears in the terminal:

<pre><code>% <span class="fg-yellow effect-blinking"><strong>WARNING</strong></span></code></pre>

This also enables you to combine text strings with different styles before printing them to the terminal. Extending the previous example:

```python linenums="1" hl_lines="4"
from colorist import style_text, Color, Effect

warning = style_text("WARNING", Color.YELLOW, Effect.BOLD, Effect.BLINK)
print(f"This is a {warning}. Be careful!")
```

How it appears in the terminal:

<pre><code>% This is a <span class="fg-yellow effect-blinking"><strong>WARNING</strong></span>. Be careful!</code></pre>
