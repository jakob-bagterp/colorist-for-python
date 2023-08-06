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
| ![Green](../../assets/images/colors/green_16x16.png) | `Color.GREEN` | ![Green text color in terminal](../../assets/images/examples/color_map/green_full_text_167x16.png) |
| ![Yellow](../../assets/images/colors/yellow_16x16.png) | `Color.YELLOW` | ![Yellow text color in terminal](../../assets/images/examples/color_map/yellow_full_text_167x16.png) |
| ![Red](../../assets/images/colors/red_16x16.png) | `Color.RED` | ![Red text color in terminal](../../assets/images/examples/color_map/red_full_text_167x16.png) |
| ![Magenta](../../assets/images/colors/magenta_16x16.png) | `Color.MAGENTA` | ![Magenta text color in terminal](../../assets/images/examples/color_map/magenta_full_text_167x16.png) |
| ![Blue](../../assets/images/colors/blue_16x16.png) | `Color.BLUE` | ![Blue text color in terminal](../../assets/images/examples/color_map/blue_full_text_167x16.png) |
| ![Cyan](../../assets/images/colors/cyan_16x16.png) | `Color.CYAN` | ![Cyan text color in terminal](../../assets/images/examples/color_map/cyan_full_text_167x16.png) |
| ![White](../../assets/images/colors/white_16x16.png) | `Color.WHITE` | ![White text color in terminal](../../assets/images/examples/color_map/white_full_text_167x16.png) |
| ![Black](../../assets/images/colors/black_16x16.png) | `Color.BLACK` | ![Black text color in terminal](../../assets/images/examples/color_map/black_full_text_167x16.png) |
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

    ![Example of white text mixed with green, yellow, red colors printed in a terminal window](../../assets/images/examples/color_custom_text_green_yellow_red.png)

!!! tip
    Remember to turn off a color with `Color.OFF` or `BrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

## `BrightColor`
Enumerable class of all available standard bright text colors.

**Options:**

| Color | Custom | Example |
| ----- | ------ | ------- |
| ![Bright green](../../assets/images/colors/bright_green_16x16.png) | `BrightColor.GREEN` | ![Bright green text color in terminal](../../assets/images/examples/color_map/bright_green_full_text_167x16.png) |
| ![Bright yellow](../../assets/images/colors/bright_yellow_16x16.png) | `BrightColor.YELLOW` | ![Bright yellow text color in terminal](../../assets/images/examples/color_map/bright_yellow_full_text_167x16.png) |
| ![Bright red](../../assets/images/colors/bright_red_16x16.png) | `BrightColor.RED` | ![Bright red text color in terminal](../../assets/images/examples/color_map/bright_red_full_text_167x16.png) |
| ![Bright magenta](../../assets/images/colors/bright_magenta_16x16.png) | `BrightColor.MAGENTA` | ![Bright magenta text color in terminal](../../assets/images/examples/color_map/bright_magenta_full_text_167x16.png) |
| ![Bright blue](../../assets/images/colors/bright_blue_16x16.png) | `BrightColor.BLUE` | ![Bright blue text color in terminal](../../assets/images/examples/color_map/bright_blue_full_text_167x16.png) |
| ![Bright cyan](../../assets/images/colors/bright_cyan_16x16.png) | `BrightColor.CYAN` | ![Bright cyan text color in terminal](../../assets/images/examples/color_map/bright_cyan_full_text_167x16.png) |
| ![Bright white](../../assets/images/colors/bright_white_16x16.png) | `BrightColor.WHITE` | ![Bright white text color in terminal](../../assets/images/examples/color_map/bright_white_full_text_167x16.png) |
| ![Bright black](../../assets/images/colors/bright_black_16x16.png) | `BrightColor.BLACK` | ![Bright black text color in terminal](../../assets/images/examples/color_map/bright_black_full_text_167x16.png) |
| - | `BrightColor.DEFAULT` | - |
| - | `BrightColor.OFF` | - |

**Example:**

???+ example
    ```python linenums="1"
    from colorist import BrightColor

    print(f"I want {BrightColor.CYAN}cyan{BrightColor.OFF} color inside this paragraph")
    ```

    How it appears in the terminal:

    ![Example of white text mixed with cyan printed in a terminal window](../../assets/images/examples/bright_color_custom_text_cyan.png)
