---
tags:
    - Features
    - Tutorial
    - Standard Colors
    - Text Colors
    - Foreground Colors
---

# Text Foreground Colors
## Introduction
When you want to print colored text in the terminal, Colorist offers two ways of doing so:

* **Full text functions:** Print a full line of colored text with the `green()`, `yellow()`, `red()`, etc. functions.
* **Custom string styling:** Mix colors to any part of a string with the `Color` and `BrightColor` classes.

## Print Line of Colored Text
How to print a full line of colored text in the terminal:

```python linenums="1"
from colorist import green, yellow, red

green("This is GREEN!")
yellow("This is YELLOW!")
red("This is RED!")
```

How it appears in the terminal:

<pre><code>% <span class="fg-green">This is GREEN!</span>
% <span class="fg-yellow">This is YELLOW!</span>
% <span class="fg-red">This is RED!</span></code></pre>

## Print Mixed Colors in Text
How to customize colors inside a paragraph and print it in the terminal:

```python linenums="1"
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")

print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
```

How it appears in the terminal:

<pre><code>% I want <span class="fg-red">red</span> color inside this paragraph
% Both <span class="fg-green">green</span> and <span class="fg-yellow">yellow</span> are nice colors</code></pre>

!!! tip
    Remember to turn off a color with `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## Bright Colors
Most terminals support bright colors that stand more out:

```python linenums="1"
from colorist import BrightColor

print(f"Put {BrightColor.CYAN}cyan{BrightColor.OFF} inside this paragraph")
```

How it appears in the terminal:

<pre><code>% Put <span class="fg-bright-cyan">cyan</span> inside this paragraph</code></pre>

Refer to the documentation for a complete list of [full line text color functions](../../reference/text-colors/full-line.md) and [custom string styling](../../reference/text-colors/mixed.md).
