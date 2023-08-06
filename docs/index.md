---
title: Home
---

# Colorist for Python 🌈
## Introduction
Lightweight Python package that makes it easy and fast to print colored text in the terminal.

## How It Works
### Basics
Colorist is intended to be easy to use. Once [installed](./getting-started/installation.md), simply import the `colorist` module and start printing colored text:

```python linenums="1"
from colorist import BrightColor

print(f"I want {BrightColor.CYAN}cyan{BrightColor.OFF} color inside this paragraph")
```

How it appears in the terminal:

![Example of white text mixed with cyan printed in a terminal window](./assets/images/examples/bright_color_custom_text_cyan.png)

Or simply print a full line of colored text:

```python linenums="1"
from colorist import bright_yellow

bright_yellow("This is BRIGHT YELLOW!")
```

How it appears in the terminal:

![Bright yellow text color in terminal](./assets/images/examples/color_map/bright_yellow_full_text_167x16.png)

Ready to try more options and features? [Let's get started](./getting-started/index.md).
