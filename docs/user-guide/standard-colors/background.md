---
tags:
    - Features
    - Tutorial
    - Background Colors
    - Standard Colors
---

# Background Colors
## Introduction
When you want to print colored backgrounds in the terminal, Colorist offers two ways of doing so:

* **Full text functions:** Print a full line of colored text with the `bg_green()`, `bg_yellow()`, `bg_red()`, etc. functions.
* **Custom string styling:** Mix colors to any part of a string with the `BgColor` and `BgBrightColor` classes.

## Print Line of Text with Background Color
How to print a full line of colored text in the terminal:

```python linenums="1"
from colorist import bg_green, bg_yellow, bg_red

bg_green("This is GREEN background!")
bg_yellow("This is YELLOW background!")
bg_red("This is RED background!")
```

How it appears in the terminal:

<pre><code>% <span class="bg-green">This is GREEN background!</span>
% <span class="bg-yellow">This is YELLOW background!</span>
% <span class="bg-red">This is RED background!</span></code></pre>

## Print Mixed Colors in Text
Background colors can also be mixed inside a paragraph:

```python linenums="1"
from colorist import BgColor

print(f"Put {BgColor.RED}red{BgColor.OFF} background color inside this paragraph")
print(f"Both {BgColor.GREEN}green{BgColor.OFF}...")
print(f"... and {BgColor.YELLOW}yellow{BgColor.OFF} are nice background colors")
```

How it appears in the terminal:

<pre><code>% Put <span class="bg-red">red</span> background color inside this paragraph
% Both <span class="bg-green">green</span>...
% ... and <span class="bg-yellow">yellow</span> are nice background colors</code></pre>

!!! tip
    Remember to turn off a color with `BgColor.OFF` or `BgBrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## Bright Colors
Most terminals support bright colors that stand more out:

```python linenums="1"
from colorist import BgBrightColor

print(f"Add {BgBrightColor.CYAN}cyan{BgBrightColor.OFF} background color")
```

How it appears in the terminal:

<pre><code>% Add <span class="bg-bright-cyan">cyan</span> background color</code></pre>

Refer to the documentation for a complete list of [full line text color functions](../../reference/background-colors/full-line.md) and [custom string styling](../../reference/background-colors/mixed.md).
