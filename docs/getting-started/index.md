---
tags:
    - Tutorial
    - Installation
    - PyPI
---

# Get Started in 2 Easy Steps 🚀
Ready to try? Let's get started:

## 1. Install Colorist for Python Package
Assuming that [Python](https://www.python.org/) is already installed, execute this command in the terminal to install the Colorist package:

```shell title=""
pip install colorist
```

Find more details and options in the [installation guide](installation.md).

## 2. First Script
You're now ready to go:

```python linenums="1"
from colorist import Color, green

green("This is GREEN!")

print(f"Both {Color.RED}red{Color.OFF}...")
print(f"... and {Color.YELLOW}yellow{Color.OFF} are nice colors")
```
How it appears in the terminal:

![Example of mixed text functions (green, yellow, red) printed in a terminal window](../assets/images/examples/mixed_text_functions.png)

## Next Steps
Find more usage examples and tutorials in the [user guide](../user-guide/index.md) section.
