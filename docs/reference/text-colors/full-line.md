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
| ![Green](../../assets/images/colors/green_16x16.png) | `green("text")` | <code><span class="fg-green">This is GREEN!</span></code> |
| ![Yellow](../../assets/images/colors/yellow_16x16.png) | `yellow("text")` | <code><span class="fg-yellow">This is YELLOW!</span></code> |
| ![Red](../../assets/images/colors/red_16x16.png) | `red("text")` | <code><span class="fg-red">This is RED!</span></code> |
| ![Magenta](../../assets/images/colors/magenta_16x16.png) | `magenta("text")` | <code><span class="fg-magenta">This is MAGENTA!</span></code> |
| ![Blue](../../assets/images/colors/blue_16x16.png) | `blue("text")` | <code><span class="fg-blue">This is BLUE!</span></code> |
| ![Cyan](../../assets/images/colors/cyan_16x16.png) | `cyan("text")` | <code><span class="fg-cyan">This is CYAN!</span></code> |
| ![White](../../assets/images/colors/white_16x16.png) | `white("text")` | <code><span class="fg-white">This is WHITE!</span></code> |
| ![Black](../../assets/images/colors/black_16x16.png) | `black("text")` | <code><span class="fg-black">This is BLACK!</span></code> |

### Bright Colors

| Color | Full Text Function | Example |
| ----- | ------------------ | ------- |
| ![Bright green](../../assets/images/colors/bright_green_16x16.png) | `bright_green("text")` | <code><span class="fg-green">This is BRIGHT GREEN!</span></code> |
| ![Bright yellow](../../assets/images/colors/bright_yellow_16x16.png) | `bright_yellow("text")` | <code><span class="fg-yellow">This is BRIGHT YELLOW!</span></code> |
| ![Bright red](../../assets/images/colors/bright_red_16x16.png) | `bright_red("text")` | <code><span class="fg-red">This is BRIGHT RED!</span></code> |
| ![Bright magenta](../../assets/images/colors/bright_magenta_16x16.png) | `bright_magenta("text")` | <code><span class="fg-magenta">This is BRIGHT MAGENTA!</span></code> |
| ![Bright blue](../../assets/images/colors/bright_blue_16x16.png) | `bright_blue("text")` | <code><span class="fg-blue">This is BRIGHT BLUE!</span></code> |
| ![Bright cyan](../../assets/images/colors/bright_cyan_16x16.png) | `bright_cyan("text")` | <code><span class="fg-cyan">This is BRIGHT CYAN!</span></code> |
| ![Bright white](../../assets/images/colors/bright_white_16x16.png) | `bright_white("text")` | <code><span class="fg-white">This is BRIGHT WHITE!</span></code> |
| ![Bright black](../../assets/images/colors/bright_black_16x16.png) | `bright_black("text")` |  <code><span class="fg-black">This is BRIGHT BLACK!</span></code> |

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

    <pre><code>% <span class="fg-green">This is GREEN!</span>
    % <span class="fg-yellow">This is YELLOW!</span>
    % <span class="fg-red">This is RED!</span></code></pre>

::: colorist.print.foreground.bright_color.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true
