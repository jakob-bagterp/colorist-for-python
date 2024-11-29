---
title: Print Text with Custom Colors
description: The easiest way to print foreground text with custom colors in terminal output using Colorist for Python. This documentation includes color maps and code examples.
tags:
    - Documentation
    - Tutorial
    - Text Colors
    - Foreground Colors
    - Standard Colors
---

# Custom String Styling for Foreground Text Colors
## `Color`
Enumerable class of all available standard text colors.

**Options:**

| Color                                                    | Color Code      | Example                                                       |
| -------------------------------------------------------- | --------------- | ------------------------------------------------------------- |
| ![Green](../../assets/images/colors/green_16x16.png)     | `Color.GREEN`   | <code><span class="fg-green">This is GREEN!</span></code>     |
| ![Yellow](../../assets/images/colors/yellow_16x16.png)   | `Color.YELLOW`  | <code><span class="fg-yellow">This is YELLOW!</span></code>   |
| ![Red](../../assets/images/colors/red_16x16.png)         | `Color.RED`     | <code><span class="fg-red">This is RED!</span></code>         |
| ![Magenta](../../assets/images/colors/magenta_16x16.png) | `Color.MAGENTA` | <code><span class="fg-magenta">This is MAGENTA!</span></code> |
| ![Blue](../../assets/images/colors/blue_16x16.png)       | `Color.BLUE`    | <code><span class="fg-blue">This is BLUE!</span></code>       |
| ![Cyan](../../assets/images/colors/cyan_16x16.png)       | `Color.CYAN`    | <code><span class="fg-cyan">This is CYAN!</span></code>       |
| ![White](../../assets/images/colors/white_16x16.png)     | `Color.WHITE`   | <code><span class="fg-white">This is WHITE!</span></code>     |
| ![Black](../../assets/images/colors/black_16x16.png)     | `Color.BLACK`   | <code><span class="fg-black">This is BLACK!</span></code>     |
| -                                                        | `Color.DEFAULT` | -                                                             |
| -                                                        | `Color.OFF`     | -                                                             |

**Example:**

???+ example
    ```python linenums="1" hl_lines="3 5"
    from colorist import Color

    print(f"I want {Color.RED}RED{Color.OFF} color inside this paragraph")

    print(f"Both {Color.GREEN}GREEN{Color.OFF} and {Color.YELLOW}YELLOW{Color.OFF} are nice colors")
    ```

    How it appears in the terminal:

    <pre><code>% I want <span class="fg-red">RED</span> color inside this paragraph
    % Both <span class="fg-green">GREEN</span> and <span class="fg-yellow">YELLOW</span> are nice colors</code></pre>

!!! tip
    Remember to turn off a color with `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## `BrightColor`
Enumerable class of all available standard bright text colors.

**Options:**

| Color                                                                  | Color Code            | Example                                                                     |
| ---------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------------------- |
| ![Bright green](../../assets/images/colors/bright_green_16x16.png)     | `BrightColor.GREEN`   | <code><span class="fg-bright-green">This is BRIGHT GREEN!</span></code>     |
| ![Bright yellow](../../assets/images/colors/bright_yellow_16x16.png)   | `BrightColor.YELLOW`  | <code><span class="fg-bright-yellow">This is BRIGHT YELLOW!</span></code>   |
| ![Bright red](../../assets/images/colors/bright_red_16x16.png)         | `BrightColor.RED`     | <code><span class="fg-bright-red">This is BRIGHT RED!</span></code>         |
| ![Bright magenta](../../assets/images/colors/bright_magenta_16x16.png) | `BrightColor.MAGENTA` | <code><span class="fg-bright-magenta">This is BRIGHT MAGENTA!</span></code> |
| ![Bright blue](../../assets/images/colors/bright_blue_16x16.png)       | `BrightColor.BLUE`    | <code><span class="fg-bright-blue">This is BRIGHT BLUE!</span></code>       |
| ![Bright cyan](../../assets/images/colors/bright_cyan_16x16.png)       | `BrightColor.CYAN`    | <code><span class="fg-bright-cyan">This is BRIGHT CYAN!</span></code>       |
| ![Bright white](../../assets/images/colors/bright_white_16x16.png)     | `BrightColor.WHITE`   | <code><span class="fg-bright-white">This is BRIGHT WHITE!</span></code>     |
| ![Bright black](../../assets/images/colors/bright_black_16x16.png)     | `BrightColor.BLACK`   | <code><span class="fg-bright-black">This is BRIGHT BLACK!</span></code>     |
| -                                                                      | `BrightColor.DEFAULT` | -                                                                           |
| -                                                                      | `BrightColor.OFF`     | -                                                                           |

**Example:**

???+ example
    ```python linenums="1" hl_lines="3"
    from colorist import BrightColor

    print(f"I want {BrightColor.CYAN}CYAN{BrightColor.OFF} color inside this paragraph")
    ```

    How it appears in the terminal:

    <pre><code>% I want <span class="fg-bright-cyan">CYAN</span> color inside this paragraph</code></pre>
