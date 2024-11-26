---
title: How to Use Backwards Compatible String Formatting
description: How Colorist for Python is backwards compatible with string formatting and concatenation. Includes code examples.
tags:
    - Features
    - Tutorial
---

# How to Use Backwards Compatible String Formatting
## F-Strings Sometimes Are Not Supported
Imagine that you want this printed in the terminal:

<pre><code>% I want <span class="fg-red">RED</span> color</code></pre>

It's often easier and more readable to use Colorist in combination with [f-strings](https://peps.python.org/pep-0498/):

```python linenums="1" hl_lines="3"
from colorist import Color

print(f"I want {Color.RED}RED{Color.OFF} color")
```

## Backwards Compatible Alternatives
But as f-strings aren't supported in some earlier versions of Python, you can instead use string formatting with `str.format()` or concatenation with `+`. All variations yield the same result as before:

<pre><code>% I want <span class="fg-red">RED</span> color</code></pre>

### String Formatting
Here's how you can use string formatting with `str.format()`:

```python linenums="1" hl_lines="3"
from colorist import Color

print("I want {0}RED{1} color".format(Color.RED, Color.OFF))
```

### String Concatenation
Here's how you can use string concatenation with `+`:

```python linenums="1" hl_lines="3"
from colorist import Color

print("I want " + Color.RED + "RED" + Color.OFF + " color")
```
