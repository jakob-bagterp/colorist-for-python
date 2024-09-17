---
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
---

# Introduction to ANSI Escape Codes
Colorist uses ANSI escape codes to style text in the terminal. This page explains how ANSI escape codes work, and how to use them in your own code.

## What Are ANSI Escape Codes?
ANSI escape sequences were introduced in the 1970s as a standard to style text terminals with color, font styling, and other options. They are supported by most modern terminals in operating systems like Windows, macOS, and Linux.

They always start with `\x1b`, `\e`, or `\033` depending on the operating system or programming language. Technically this inserts byte 27 into a string, which is equivalent to `0x1b` and the `ESC` key when you look at an [ASCII table](https://www.asciitable.com). Hence the name.

Though ANSI escape sequences appear in a string as multiple characters, they are in reality interpreted by the terminal as a single command. For example:

* `\x1b[31m`: Change the color to red
* `\x1b[0m`: Reset any styling

How to apply this in a print command:

```python
print(f"I want \x1b[31mred\x1b[0m color inside this paragraph")
```

And yet, the characters of the sequences are hidden in the terminal output apart from the color change:

<pre><code>% I want <span class="fg-red">red</span> color inside this paragraph</code></pre>

## Humanised Sequences
This is also why it's [convenient to use Colorist](../user-guide/standard-colors/text-foreground.md) instead of manually writing raw ANSI escape codes. The `Color` class will generate the ANSI escape sequences and keep the code readable. This example generates the same terminal output as above:

```python
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")
```
