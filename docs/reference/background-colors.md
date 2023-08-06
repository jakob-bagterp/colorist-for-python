---
tags:
    - Documentation
    - Tutorial
---

# Background Colors
## Full Text Functions
### Examples
#### Normal Colors

| Color | Full Text Function | Example |
| ----- | ------------------ | ------- |
| ![Green](../assets/images/colors/green_16x16.png) | `bg_green("text")` | | ![Green background color in terminal](../assets/images/examples/bg_color_map/green_full_text_194x16.png) |
| ![Yellow](../assets/images/colors/yellow_16x16.png) | `bg_yellow("text")` | ![Yellow background color in terminal](../assets/images/examples/bg_color_map/yellow_full_text_194x16.png) |
| ![Red](../assets/images/colors/red_16x16.png) | `bg_red("text")` | ![Red background color in terminal](../assets/images/examples/bg_color_map/red_full_text_194x16.png) |
| ![Magenta](../assets/images/colors/magenta_16x16.png) | `bg_magenta("text")` | ![Magenta background color in terminal](../assets/images/examples/bg_color_map/magenta_full_text_194x16.png) |
| ![Blue](../assets/images/colors/blue_16x16.png) | `bg_blue("text")` | ![Blue background color in terminal](../assets/images/examples/bg_color_map/blue_full_text_194x16.png) |
| ![Cyan](../assets/images/colors/cyan_16x16.png) | `bg_cyan("text")` | ![Cyan background color in terminal](../assets/images/examples/bg_color_map/cyan_full_text_194x16.png) |
| ![White](../assets/images/colors/white_16x16.png) | `bg_white("text")` | ![White background color in terminal](../assets/images/examples/bg_color_map/white_full_text_194x16.png) |
| ![Black](../assets/images/colors/black_16x16.png) | `bg_black("text")` | ![Black background color in terminal](../assets/images/examples/bg_color_map/black_full_text_194x16.png) |

#### Bright Colors

| Color | Full Text Function | Example |
| ----- | ------------------ | ------- |
| ![Bright green](../assets/images/colors/bright_green_16x16.png) | `bg_bright_green("text")` | ![Bright green background color in terminal](../assets/images/examples/bg_color_map/bright_green_full_text_194x16.png) |
| ![Bright yellow](../assets/images/colors/bright_yellow_16x16.png) | `bg_bright_yellow("text")` | ![Bright yellow background color in terminal](../assets/images/examples/bg_color_map/bright_yellow_full_text_194x16.png) |
| ![Bright red](../assets/images/colors/bright_red_16x16.png) | `bg_bright_red("text")` | ![Bright red background color in terminal](../assets/images/examples/bg_color_map/bright_red_full_text_194x16.png) |
| ![Bright magenta](../assets/images/colors/bright_magenta_16x16.png) | `bg_bright_magenta("text")` | ![Bright magenta background color in terminal](../assets/images/examples/bg_color_map/bright_magenta_full_text_194x16.png) |
| ![Bright blue](../assets/images/colors/bright_blue_16x16.png) | `bg_bright_blue("text")` | ![Bright blue background color in terminal](../assets/images/examples/bg_color_map/bright_blue_full_text_194x16.png) |
| ![Bright cyan](../assets/images/colors/bright_cyan_16x16.png) | `bg_bright_cyan("text")` | ![Bright cyan background color in terminal](../assets/images/examples/bg_color_map/bright_cyan_full_text_194x16.png) |
| ![Bright white](../assets/images/colors/bright_white_16x16.png) | `bg_bright_white("text")` | ![Bright white background color in terminal](../assets/images/examples/bg_color_map/bright_white_full_text_194x16.png) |
| ![Bright black](../assets/images/colors/bright_black_16x16.png) | `bg_bright_black("text")` | ![Bright black background color in terminal](../assets/images/examples/bg_color_map/bright_black_full_text_194x16.png) |

!!! note "Limited Support for Bright Colors"
    Note that bright colors are [supported by many terminals](../user-guide/terminal-support.md), but not all as bright colors aren't part of the standard set of ANSI colors.

::: colorist.print.background.color.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true

???+ example

    ```python linenums="1"
    from colorist import bg_green, bg_yellow, bg_red

    bg_green("This is GREEN background!")
    bg_yellow("This is YELLOW background!")
    bg_red("This is RED background!")
    ```

    How it appears in the terminal:

    ![Example of white text and colored backgrounds if green, yellow, red printed in a terminal window](../assets/images/examples/bg_color_full_text_green_yellow_red.png)

::: colorist.print.background.bright_color.MkDocstringsWrapper
    options:
      show_category_heading: false
      heading_level: 3
      merge_init_into_class: true

## Custom String Styling
### `BgColor`
Enumerable class of all available standard background colors.

**Options:**

| Color | Custom | Example |
| ----- | ------ | ------- |
| ![Green](../assets/images/colors/green_16x16.png) | `BgColor.GREEN` | ![Green background color in terminal](../assets/images/examples/bg_color_map/green_full_text_194x16.png) |
| ![Yellow](../assets/images/colors/yellow_16x16.png) | `BgColor.YELLOW` | ![Yellow background color in terminal](../assets/images/examples/bg_color_map/yellow_full_text_194x16.png) |
| ![Red](../assets/images/colors/red_16x16.png) | `BgColor.RED` | ![Red background color in terminal](../assets/images/examples/bg_color_map/red_full_text_194x16.png) |
| ![Magenta](../assets/images/colors/magenta_16x16.png) | `BgColor.MAGENTA` | ![Magenta background color in terminal](../assets/images/examples/bg_color_map/magenta_full_text_194x16.png) |
| ![Blue](../assets/images/colors/blue_16x16.png) | `BgColor.BLUE` | ![Blue background color in terminal](../assets/images/examples/bg_color_map/blue_full_text_194x16.png) |
| ![Cyan](../assets/images/colors/cyan_16x16.png) | `BgColor.CYAN` | ![Cyan background color in terminal](../assets/images/examples/bg_color_map/cyan_full_text_194x16.png) |
| ![White](../assets/images/colors/white_16x16.png) | `BgColor.WHITE` | ![White background color in terminal](../assets/images/examples/bg_color_map/white_full_text_194x16.png) |
| ![Black](../assets/images/colors/black_16x16.png) | `BgColor.BLACK` | ![Black background color in terminal](../assets/images/examples/bg_color_map/black_full_text_194x16.png) |
| - | `BgColor.DEFAULT` | - |
| - | `BgColor.OFF` | - |

**Example:**

???+ example
    ```python linenums="1"
    from colorist import BgColor

    print(f"I want {BgColor.RED}red{BgColor.OFF} background color inside this paragraph")

    print(f"Both {BgColor.GREEN}green{BgColor.OFF} and {BgColor.YELLOW}yellow{BgColor.OFF} are nice background colors")
    ```

    How it appears in the terminal:

    ![Example of black, green, yellow, red background colors mixed inside paragraph printed in a terminal window](../assets/images/examples/bg_color_custom_text_green_yellow_red.png)

!!! tip
    Remember to turn off a color with `BgColor.OFF` or `BgBrightColor.OFF` every time you want to revert back to the default terminal text style. Otherwise, the effect may spill over and into other terminal messages.

### `BgBrightColor`
Enumerable class of all available standard bright background colors.

**Options:**

| Color | Custom | Example |
| ----- | ------ | ------- |
| ![Bright green](../assets/images/colors/bright_green_16x16.png) | `BgBrightColor.GREEN` | ![Bright green background color in terminal](../assets/images/examples/bg_color_map/bright_green_full_text_194x16.png) |
| ![Bright yellow](../assets/images/colors/bright_yellow_16x16.png) | `BgBrightColor.YELLOW` | ![Bright yellow background color in terminal](../assets/images/examples/bg_color_map/bright_yellow_full_text_194x16.png) |
| ![Bright red](../assets/images/colors/bright_red_16x16.png) | `BgBrightColor.RED` | ![Bright red background color in terminal](../assets/images/examples/bg_color_map/bright_red_full_text_194x16.png) |
| ![Bright magenta](../assets/images/colors/bright_magenta_16x16.png) | `BgBrightColor.MAGENTA` | ![Bright magenta background color in terminal](../assets/images/examples/bg_color_map/bright_magenta_full_text_194x16.png) |
| ![Bright blue](../assets/images/colors/bright_blue_16x16.png) | `BgBrightColor.BLUE` | ![Bright blue background color in terminal](../assets/images/examples/bg_color_map/bright_blue_full_text_194x16.png) |
| ![Bright cyan](../assets/images/colors/bright_cyan_16x16.png) | `BgBrightColor.CYAN` | ![Bright cyan background color in terminal](../assets/images/examples/bg_color_map/bright_cyan_full_text_194x16.png) |
| ![Bright white](../assets/images/colors/bright_white_16x16.png) | `BgBrightColor.WHITE` | ![Bright white background color in terminal](../assets/images/examples/bg_color_map/bright_white_full_text_194x16.png) |
| ![Bright black](../assets/images/colors/bright_black_16x16.png) | `BgBrightColor.BLACK` | ![Bright black background color in terminal](../assets/images/examples/bg_color_map/bright_black_full_text_194x16.png) |
| - | `BgBrightColor.DEFAULT` | - |
| - | `BgBrightColor.OFF` | - |

**Example:**

???+ example
    ```python linenums="1"
    from colorist import BgBrightColor

    print(f"I want {BgBrightColor.CYAN}cyan{BgBrightColor.OFF} background color inside this paragraph")
    ```

    How it appears in the terminal:

    ![Example of white text on a cyan background color printed in a terminal window](../assets/images/examples/bg_bright_color_custom_text_cyan.png)
