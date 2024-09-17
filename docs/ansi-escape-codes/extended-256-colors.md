---
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
    - Extended 256 Colors
---

# Extended 256 Colors in ANSI Escape Codes
The [extended palette of 256 colors](https://commons.wikimedia.org/wiki/File:Xterm_256color_chart.svg) is a 6x6x6 color cube, with 216 colors, plus 24 shades of gray. The color cube is made up of 6 levels of red, green, and blue, respectively. The color cube is then combined with the 24 shades of gray to make up the 256 colors.

It works both with foreground text and background colors. Simply replace the two underscores `__` with any number from `0` to `255`:

| Code            | Placement  |
| :-------------: | :--------: |
| `\x1b[38;5;__m` | Text       |
| `\x1b[48;5;__m` | Background |

For example, `\x1b[38;5;243m` is a light gray foreground text color, and `\x1b[48;5;243m` is a light gray background color.
