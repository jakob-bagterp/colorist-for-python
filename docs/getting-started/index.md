---
title: Get Started in 2 Easy Steps
description: Quick guide to installing and using Colorist for Python, so you can add color to your terminal output in just 2 easy steps. Includes code examples.
tags:
    - Tutorial
    - Installation
    - PyPI
---

# Get Started with Colorist in 2 Easy Steps 🚀
Ready to try the easy way to add color to your Python code? Let's get started:

## 1. Install Colorist for Python Package
Assuming that [Python](https://www.python.org/) is already installed, execute this command in the terminal to install the Colorist package:

```shell title=""
pip install colorist
```

Find more details and options in the [installation guide](installation.md).

## 2. First Script
You're now ready to go:

```python linenums="1" hl_lines="3-5"
from colorist import Color, green

green("This is GREEN!")
print(f"Both {Color.RED}RED{Color.OFF}...")
print(f"... and {Color.YELLOW}YELLOW{Color.OFF} are nice colors")
```

How it appears in the terminal:

<pre><code>% <span class="fg-green">This is GREEN!</span>
% Both <span class="fg-red">RED</span>...
% ... and <span class="fg-yellow">YELLOW</span> are nice colors</code></pre>

## Next Steps
Find more usage examples and tutorials in the [user guide](../user-guide/index.md) section.

## Support the Project
If you have already downloaded and tried the package, perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
