# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import (bg_bright_black, bg_bright_blue, bg_bright_cyan, bg_bright_green, bg_bright_magenta,
                      bg_bright_red, bg_bright_white, bg_bright_yellow)

if __name__ == "__main__":
    print("")
    bg_bright_green("This is GREEN background!")
    print("")
    bg_bright_yellow("This is YELLOW background!")
    print("")
    bg_bright_red("This is RED background!")
    print("")
    bg_bright_magenta("This is MAGENTA background!")
    print("")
    bg_bright_blue("This is BLUE background!")
    print("")
    bg_bright_cyan("This is CYAN background!")
    print("")
    bg_bright_white("This is WHITE background!")
    print("")
    bg_bright_black("This is BLACK background!")
    print("")
