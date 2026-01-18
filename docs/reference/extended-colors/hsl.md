---
title: Print Text with HSL Colors
description: The easiest way to print text with 24-bit RGB colors in terminal output using HSL and Colorist for Python. The documentation includes code examples.
tags:
    - Documentation
    - Tutorial
    - Extended Colors
    - HSL Colors
---

# HSL Colors
!!! info "Disclaimer"
    Not all [terminals support](../../user-guide/compatibility/terminal-support.md) 24-bit colors in RGB, HSL, Hex, or OKLCH. If your terminal does support such advanced colors, read on.

## Full Line Text Functions

::: colorist.print.foreground.hsl.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 4
      merge_init_into_class: true

::: colorist.print.background.hsl.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 4
      merge_init_into_class: true

## Custom String Styling
### `ColorHSL(hue, saturation, lightness)`
::: colorist.ColorHSL
    options:
      show_category_heading: false
      heading_level: 4
      merge_init_into_class: true

### `BgColorHSL(hue, saturation, lightness)`
::: colorist.BgColorHSL
    options:
      show_category_heading: false
      heading_level: 4
      merge_init_into_class: true
