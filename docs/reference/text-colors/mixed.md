---
tags:
    - Documentation
    - Tutorial
---

# Custom String Styling for Foreground Text Colors
## `Color`
Enumerable class of all available standard text colors.

**Options:**

| Color | Custom | Example |
| ----- | ------ | ------- |
| ![Green](../../assets/images/colors/green_16x16.png) | `Color.GREEN` | <code><font color="lawngreen">This is GREEN!</font></code> |
| ![Yellow](../../assets/images/colors/yellow_16x16.png) | `Color.YELLOW` | <code><font color="yellow">This is YELLOW!</font></code> |
| ![Red](../../assets/images/colors/red_16x16.png) | `Color.RED` | <code><font color="red">This is RED!</font></code> |
| ![Magenta](../../assets/images/colors/magenta_16x16.png) | `Color.MAGENTA` | <code><font color="magenta">This is MAGENTA!</font></code> |
| ![Blue](../../assets/images/colors/blue_16x16.png) | `Color.BLUE` | <code><font color="blue">This is BLUE!</font></code> |
| ![Cyan](../../assets/images/colors/cyan_16x16.png) | `Color.CYAN` | <code><font color="cyan">This is CYAN!</font></code> |
| ![White](../../assets/images/colors/white_16x16.png) | `Color.WHITE` | <code><font color="white">This is WHITE!</font></code> |
| ![Black](../../assets/images/colors/black_16x16.png) | `Color.BLACK` | <code><font color="black">This is BLACK!</font></code> |
| - | `Color.DEFAULT` | - |
| - | `Color.OFF` | - |

**Example:**

???+ example
    ```python linenums="1"
    from colorist import Color

    print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")

    print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
    ```

    How it appears in the terminal:

    <pre><code>% I want <font color="red">red</font> color inside this paragraph
    % Both <font color="lawngreen">green</font> and <font color="yellow">yellow</font> are nice colors</code></pre>

!!! tip
    Remember to turn off a color with `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## `BrightColor`
Enumerable class of all available standard bright text colors.

**Options:**

| Color | Custom | Example |
| ----- | ------ | ------- |
| ![Bright green](../../assets/images/colors/bright_green_16x16.png) | `BrightColor.GREEN` | <code><font color="lawngreen">This is BRIGHT GREEN!</font></code> |
| ![Bright yellow](../../assets/images/colors/bright_yellow_16x16.png) | `BrightColor.YELLOW` | <code><font color="yellow">This is BRIGHT YELLOW!</font></code> |
| ![Bright red](../../assets/images/colors/bright_red_16x16.png) | `BrightColor.RED` | <code><font color="red">This is BRIGHT RED!</font></code> |
| ![Bright magenta](../../assets/images/colors/bright_magenta_16x16.png) | `BrightColor.MAGENTA` | <code><font color="magenta">This is BRIGHT MAGENTA!</font></code> |
| ![Bright blue](../../assets/images/colors/bright_blue_16x16.png) | `BrightColor.BLUE` | <code><font color="blue">This is BRIGHT BLUE!</font></code> |
| ![Bright cyan](../../assets/images/colors/bright_cyan_16x16.png) | `BrightColor.CYAN` | <code><font color="cyan">This is BRIGHT CYAN!</font></code> |
| ![Bright white](../../assets/images/colors/bright_white_16x16.png) | `BrightColor.WHITE` | <code><font color="white">This is BRIGHT WHITE!</font></code> |
| ![Bright black](../../assets/images/colors/bright_black_16x16.png) | `BrightColor.BLACK` | <code><font color="black">This is BRIGHT BLACK!</font></code> |
| - | `BrightColor.DEFAULT` | - |
| - | `BrightColor.OFF` | - |

**Example:**

???+ example
    ```python linenums="1"
    from colorist import BrightColor

    print(f"I want {BrightColor.CYAN}cyan{BrightColor.OFF} color inside this paragraph")
    ```

    How it appears in the terminal:

    <pre><code>% I want <font color="cyan">cyan</font> color inside this paragraph</code></pre>
