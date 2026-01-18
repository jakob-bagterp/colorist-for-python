---
title: Print Text with OKLCH Colors
description: The easiest way to print text with OKLCH colors in terminal output using Colorist for Python. This documentation includes code examples.
tags:
    - Documentation
    - Tutorial
    - Extended Colors
    - OKLCH Colors
---

# OKLCH Colors
!!! info "Disclaimer"
    Not all [terminals support](../../user-guide/compatibility/terminal-support.md) 24-bit colors in RGB, HSL, Hex, or OKLCH. If your terminal does support such advanced colors, read on.

## Full Line Text Functions

::: colorist.print.foreground.oklch.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 4
      merge_init_into_class: true

::: colorist.print.background.oklch.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 4
      merge_init_into_class: true

## Custom String Styling
### `ColorOKLCH(lightness, chroma, hue)`
::: colorist.ColorOKLCH
    options:
      show_category_heading: false
      heading_level: 4
      merge_init_into_class: true

### `BgColorOKLCH(lightness, chroma, hue)`
::: colorist.BgColorOKLCH
    options:
      show_category_heading: false
      heading_level: 4
      merge_init_into_class: true
