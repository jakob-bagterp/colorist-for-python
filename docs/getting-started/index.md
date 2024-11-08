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

<pre><code>% <span class="fg-green">This is GREEN!</span>
% Both <span class="fg-red">red</span>...
% ... and <span class="fg-yellow">yellow</span> are nice colors</code></pre>

## Next Steps
Find more usage examples and tutorials in the [user guide](../user-guide/index.md) section.

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
