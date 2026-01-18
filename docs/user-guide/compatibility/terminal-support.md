---
title: Supported Colors and Styles by Terminals
description: Not all terminals support all types of ANSI escape codes. Get a list of which Colorist methods are supported by which terminals.
tags:
    - Documentation
---

# Supported Colors and Styles by Terminals
## Limited Support for ANSI Escape Codes
Colorist is based on [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code), a standard that defines colors, styling, and effects for text in terminal windows. Note that most terminals support all color options, but not all.

## Overview
Generally, the features of Colorist are supported in these categories:

<div id="terminals-color-support-table"></div>

| Category                                        | Supported By                                  | Colorist Options[^1]                                                                                       |
| ----------------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Standard ANSI colors and effects                | :material-check-all: Almost all terminals     | `Color`, `BgColor`, `Effect`                                                                               |
| Non-standard ANSI, bright, and 8-bit VGA colors | :material-check: Most terminals               | `BrightColor`, `BgBrightColor`, `ColorVGA`, `BgColorVGA`                                                   |
| Advanced ANSI colors such as 24-bit RGB colors  | :material-help-circle-outline: Some terminals | `ColorRGB`, `BgColorRGB`, `ColorHSL`, `BgColorHSL`, `ColorHex`, `BgColorHex`, `ColorOKLCH`, `BgColorOKLCH` |

Refer to the terminal's documentation to see if it supports extended color palettes.

[^1]: Only custom string styling methods are mentioned in this overview. However, this similarly applies to the respective full text functions. For instance `vga()` for `ColorVGA`, `bg_vga()` for `BgColorVGA`,  `rgb()` for `ColorRGB`, `bg_rgb()` for `BgColorRGB`, etc.
