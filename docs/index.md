---
title: Add Color to Your Terminal
description: Colorist is a lightweight Python package that makes it easy and fast to print colored text in the terminal.
---

[![Latest version](https://img.shields.io/static/v1?label=version&message=1.8.6&color=yellowgreen)](https://github.com/jakob-bagterp/colorist-for-python/releases/latest)
[![Python 3.10 | 3.11 | 3.12 | 3.13 | 3.14+](https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11%20|%203.12%20|%203.13%20|%203.14%2B&color=blueviolet)](https://www.python.org)
[![BSD-3-Clause license](https://img.shields.io/static/v1?label=license&message=BSD-3-Clause&color=blue)](https://github.com/jakob-bagterp/colorist-for-python/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/colorist-for-python/branch/master/graph/badge.svg?token=1E69VOP4ED)](https://codecov.io/gh/jakob-bagterp/colorist-for-python)
[![CodeQL](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/github-code-scanning/codeql)
[![Test](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/colorist)](https://pepy.tech/project/colorist)

# Colorist for Python 🌈
## What Is Colorist?
Lightweight Python package that makes it easy and fast to print colored text in the terminal.

<div class="color-cubes">
    <img src="assets/images/cubes/cube_bright.svg" alt="Color cube bright">
    <img src="assets/images/cubes/cube_dark.svg" alt="Color cube dark">
</div>

## How It Works
### Basic Usage
Colorist is intended to be easy to use. Imagine you want to print a mix of colors in the terminal:

<pre><code>% This is <span class="fg-red">RED</span>!</code></pre>

Once [installed](getting-started/installation.md), simply import the `colorist` module and start printing colored text with the `Color` class:

```python linenums="1" hl_lines="3"
from colorist import Color

print(f"This is {Color.RED}RED{Color.OFF}!")
```

You can use the same method to [apply other colors to text](user-guide/standard-colors/text-foreground.md).

### Varied Color Palette
Or simply print a full line of colored text from a varied [palette of colors](user-guide/standard-colors/text-foreground.md#print-line-of-colored-text):

```python linenums="1" hl_lines="3-6"
from colorist import bright_magenta, bright_yellow, blue, green

cyan("This is BLUE!")
green("This is GREEN!")
bright_magenta("This is BRIGHT MAGENTA!")
bright_yellow("This is BRIGHT YELLOW!")
```

How it appears in the terminal:

<pre><code>% <span class="fg-blue">This is BLUE!</span>
% <span class="fg-green">This is GREEN!</span>
% <span class="fg-bright-magenta">This is BRIGHT MAGENTA!</span>
% <span class="fg-bright-yellow">This is BRIGHT YELLOW!</span></code></pre>

### Background Colors
It's also possible to apply [background colors](user-guide/standard-colors/background.md) to text:

```python linenums="1" hl_lines="3"
from colorist import BgColor

print(f"This is {BgColor.RED}RED{BgColor.OFF}!")
```

How it appears in the terminal:

<pre><code>% This is <span class="bg-red text-contrast">RED</span>!</code></pre>

You can use the same method to [apply other background colors](user-guide/standard-colors/background.md) to text.

## Next Steps
Ready to try more options and features? Let's get started with the [installation](getting-started/index.md) or check out the [user guide](user-guide/index.md).

## Support the Project
If you have already downloaded and tried the package – maybe even used it in a production environment – perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
