---
title: Home
---

[![Latest version](https://img.shields.io/static/v1?label=version&message=1.7.1&color=yellowgreen)](https://github.com/jakob-bagterp/colorist-for-python/releases/latest)
[![Python 3.10 | 3.11 | 3.12 or higher](https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11%20|%203.12%2B&color=blueviolet)](https://www.python.org)
[![BSD-3-Clause license](https://img.shields.io/static/v1?label=license&message=BSD-3-Clause&color=blue)](https://github.com/jakob-bagterp/colorist-for-python/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/colorist-for-python/branch/master/graph/badge.svg?token=1E69VOP4ED)](https://codecov.io/gh/jakob-bagterp/colorist-for-python)
[![CodeQL](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/codeql.yml/badge.svg)](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/codeql.yml)
[![Test](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/colorist-for-python/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/colorist)](https://pepy.tech/project/colorist)

# Colorist for Python 🌈
## Introduction
Lightweight Python package that makes it easy and fast to print colored text in the terminal.

## How It Works
### Basics
Colorist is intended to be easy to use. Imagine you want to print a mix of colors in the terminal:

<pre><code>% This is <span class="fg-red">RED</span>!</code></pre>

Once [installed](./getting-started/installation.md), simply import the `colorist` module and start printing colored text with the `Color` class:

```python linenums="1"
from colorist import Color

print(f"This is {Color.RED}RED{Color.OFF}!")
```

### Varied Color Palette
Or simply print a full line of colored text from a varied [palette of color](./user-guide/standard-colors/text-foreground.md#print-line-of-colored-text):

```python linenums="1"
from colorist import bright_yellow

bright_yellow("This is BRIGHT YELLOW!")
```

How it appears in the terminal:

<pre><code>% <span class="fg-bright-yellow">This is BRIGHT YELLOW!</span></code></pre>

Ready to try more options and features? [Let's get started](./getting-started/index.md).
