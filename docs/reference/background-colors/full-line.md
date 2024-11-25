---
title: Print Colored Background Text
description: The easiest way to print colored background text in terminal output using Colorist for Python. This documentation includes color maps and code examples.
tags:
    - Documentation
    - Tutorial
    - Background Colors
    - Standard Colors
---

# Full Line Text Functions for Background Colors
## Color Maps
### Normal Colors

| Color                                                    | Full Text Function   | Example                                                                  |
| -------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------ |
| ![Green](../../assets/images/colors/green_16x16.png)     | `bg_green("text")`   | <code><span class="bg-green">This is GREEN background!</span></code>     |
| ![Yellow](../../assets/images/colors/yellow_16x16.png)   | `bg_yellow("text")`  | <code><span class="bg-yellow">This is YELLOW background!</span></code>   |
| ![Red](../../assets/images/colors/red_16x16.png)         | `bg_red("text")`     | <code><span class="bg-red">This is RED background!</span></code>         |
| ![Magenta](../../assets/images/colors/magenta_16x16.png) | `bg_magenta("text")` | <code><span class="bg-magenta">This is MAGENTA background!</span></code> |
| ![Blue](../../assets/images/colors/blue_16x16.png)       | `bg_blue("text")`    | <code><span class="bg-blue">This is BLUE background!</span></code>       |
| ![Cyan](../../assets/images/colors/cyan_16x16.png)       | `bg_cyan("text")`    | <code><span class="bg-cyan">This is CYAN background!</span></code>       |
| ![White](../../assets/images/colors/white_16x16.png)     | `bg_white("text")`   | <code><span class="bg-white">This is WHITE background!</span></code>     |
| ![Black](../../assets/images/colors/black_16x16.png)     | `bg_black("text")`   | <code><span class="bg-black">This is BLACK background!</span></code>     |

???+ example

    ```python linenums="1" hl_lines="3-5"
    from colorist import bg_green, bg_yellow, bg_red

    bg_green("This is GREEN background!")
    bg_yellow("This is YELLOW background!")
    bg_red("This is RED background!")
    ```

    How it appears in the terminal:

    <pre><code>% <span class="bg-green">This is GREEN background!</span>
    % <span class="bg-yellow">This is YELLOW background!</span>
    % <span class="bg-red">This is RED background!</span></code></pre>

### Bright Colors

| Color                                                                  | Full Text Function          | Example                                                                                              |
| ---------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------- |
| ![Bright green](../../assets/images/colors/bright_green_16x16.png)     | `bg_bright_green("text")`   | <code><span class="bg-bright-green">This is BRIGHT GREEN background!</span></code>     |
| ![Bright yellow](../../assets/images/colors/bright_yellow_16x16.png)   | `bg_bright_yellow("text")`  | <code><span class="bg-bright-yellow">This is BRIGHT YELLOW background!</span></code>   |
| ![Bright red](../../assets/images/colors/bright_red_16x16.png)         | `bg_bright_red("text")`     | <code><span class="bg-bright-red">This is BRIGHT RED background!</span></code>         |
| ![Bright magenta](../../assets/images/colors/bright_magenta_16x16.png) | `bg_bright_magenta("text")` | <code><span class="bg-bright-magenta">This is BRIGHT MAGENTA background!</span></code> |
| ![Bright blue](../../assets/images/colors/bright_blue_16x16.png)       | `bg_bright_blue("text")`    | <code><span class="bg-bright-blue">This is BRIGHT BLUE background!</span></code>       |
| ![Bright cyan](../../assets/images/colors/bright_cyan_16x16.png)       | `bg_bright_cyan("text")`    | <code><span class="bg-bright-cyan">This is BRIGHT CYAN background!</span></code>       |
| ![Bright white](../../assets/images/colors/bright_white_16x16.png)     | `bg_bright_white("text")`   | <code><span class="bg-bright-white">This is BRIGHT WHITE background!</span></code>     |
| ![Bright black](../../assets/images/colors/bright_black_16x16.png)     | `bg_bright_black("text")`   | <code><span class="bg-bright-black">This is BRIGHT BLACK background!</span></code>     |

!!! note "Limited Support for Bright Colors"
    Note that bright colors are [supported by many terminals](../../user-guide/materials/terminal-support.md), yet not all as bright colors aren't part of the standard set of ANSI colors.

???+ example

    ```python linenums="1" hl_lines="3-5"
    from colorist import bg_bright_green, bg_bright_yellow, bg_bright_red

    bg_bright_green("This is BRIGHT GREEN background!")
    bg_bright_yellow("This is BRIGHT YELLOW background!")
    bg_bright_red("This is BRIGHT RED background!")
    ```

    How it appears in the terminal:

    <pre><code>% <span class="bg-bright-green">This is BRIGHT GREEN background!</span>
    % <span class="bg-bright-yellow">This is BRIGHT YELLOW background!</span>
    % <span class="bg-bright-red">This is BRIGHT RED background!</span></code></pre>

## Functions

::: colorist.print.background.color.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true

::: colorist.print.background.bright_color.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true
