---
title: Guide to Other String Formats
description: How Colorist for Python is backwards compatible with string formatting and concatenation. Includes code examples.
tags:
    - Features
    - Tutorial
---

# Other String Formats
## How to Apply String Formatting and Concatenation
Imagine that you want this printed in the terminal:

<pre><code>% I want <span class="fg-red">red</span> color</code></pre>

It's often easier and more readable to use Colorist in combination with [f-strings](https://peps.python.org/pep-0498/):

```python linenums="1" hl_lines="3"
from colorist import Color

print(f"I want {Color.RED}red{Color.OFF} color")
```

But as f-strings aren't supported in some earlier versions of Python, you can instead use string formatting with `str.format()` or concatenation with `+`. All variations yield the same result as above:

```python linenums="1" hl_lines="3 5"
from colorist import Color

print("I want {0}red{1} color".format(Color.RED, Color.OFF))

print("I want " + Color.RED + "red" + Color.OFF + " color")
```
