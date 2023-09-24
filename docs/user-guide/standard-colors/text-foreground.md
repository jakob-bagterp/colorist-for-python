---
tags:
    - Features
    - Tutorial
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

<pre><code>% <font color="lawngreen">This is GREEN!</font>
% <font color="yellow">This is YELLOW!</font>
% <font color="red">This is RED!</font></code></pre>

## Print Mixed Colors in Text
How to customize colors inside a paragraph and print it in the terminal:

```python linenums="1"
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")

print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
```

How it appears in the terminal:

<pre><code>% I want <font color="red">red</font> color inside this paragraph
% Both <font color="lawngreen">green</font> and <font color="yellow">yellow</font> are nice colors</code></pre>

!!! tip
    Remember to turn off a color with `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## Bright Colors
Most terminals support bright colors that stand more out:

```python linenums="1"
from colorist import BrightColor

print(f"Put {BrightColor.CYAN}cyan{BrightColor.OFF} inside this paragraph")
```

How it appears in the terminal:

<pre><code>% Put <font color="cyan">cyan</font> inside this paragraph</code></pre>

Refer to the documentation for a complete list of [full line text color functions](../../reference/text-colors/full-line.md) and [custom string styling](../../reference/text-colors/mixed.md).
