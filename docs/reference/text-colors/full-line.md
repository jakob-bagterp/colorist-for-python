---
tags:
    - Documentation
    - Tutorial
---

# Full Text Functions for Foreground Colors
## Examples
### Normal Colors

| Color | Full Text Function | Example |
| ----- | ------------------ | ------- |
| ![Green](../../assets/images/colors/green_16x16.png) | `green("text")` | <code><font color="lawngreen">This is GREEN!</font></code> |
| ![Yellow](../../assets/images/colors/yellow_16x16.png) | `yellow("text")` | <code><font color="yellow">This is YELLOW!</font></code> |
| ![Red](../../assets/images/colors/red_16x16.png) | `red("text")` | <code><font color="red">This is RED!</font></code> |
| ![Magenta](../../assets/images/colors/magenta_16x16.png) | `magenta("text")` | <code><font color="magenta">This is MAGENTA!</font></code> |
| ![Blue](../../assets/images/colors/blue_16x16.png) | `blue("text")` | <code><font color="blue">This is BLUE!</font></code> |
| ![Cyan](../../assets/images/colors/cyan_16x16.png) | `cyan("text")` | <code><font color="cyan">This is CYAN!</font></code> |
| ![White](../../assets/images/colors/white_16x16.png) | `white("text")` | <code><font color="white">This is WHITE!</font></code> |
| ![Black](../../assets/images/colors/black_16x16.png) | `black("text")` | <code><font color="black">This is BLACK!</font></code> |

### Bright Colors

| Color | Full Text Function | Example |
| ----- | ------------------ | ------- |
| ![Bright green](../../assets/images/colors/bright_green_16x16.png) | `bright_green("text")` | <code><font color="lawngreen">This is BRIGHT GREEN!</font></code> |
| ![Bright yellow](../../assets/images/colors/bright_yellow_16x16.png) | `bright_yellow("text")` | <code><font color="yellow">This is BRIGHT YELLOW!</font></code> |
| ![Bright red](../../assets/images/colors/bright_red_16x16.png) | `bright_red("text")` | <code><font color="red">This is BRIGHT RED!</font></code> |
| ![Bright magenta](../../assets/images/colors/bright_magenta_16x16.png) | `bright_magenta("text")` | <code><font color="magenta">This is BRIGHT MAGENTA!</font></code> |
| ![Bright blue](../../assets/images/colors/bright_blue_16x16.png) | `bright_blue("text")` | <code><font color="blue">This is BRIGHT BLUE!</font></code> |
| ![Bright cyan](../../assets/images/colors/bright_cyan_16x16.png) | `bright_cyan("text")` | <code><font color="cyan">This is BRIGHT CYAN!</font></code> |
| ![Bright white](../../assets/images/colors/bright_white_16x16.png) | `bright_white("text")` | <code><font color="white">This is BRIGHT WHITE!</font></code> |
| ![Bright black](../../assets/images/colors/bright_black_16x16.png) | `bright_black("text")` |  <code><font color="black">This is BRIGHT BLACK!</font></code> |

!!! note "Limited Support for Bright Colors"
    Note that bright colors are [supported by many terminals](../../user-guide/materials/terminal-support.md), but not all as bright colors aren't part of the standard set of ANSI colors.

## Functions

::: colorist.print.foreground.color.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true

???+ example
    ```python linenums="1"
    from colorist import green, yellow, red

    green("This is GREEN!")
    yellow("This is YELLOW!")
    red("This is RED!")
    ```

    How it appears in the terminal:

    <pre><code>% <font color="lawngreen">This is GREEN!</font>
    % <font color="yellow">This is YELLOW!</font>
    % <font color="red">This is RED!</font></code></pre>

::: colorist.print.foreground.bright_color.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true
