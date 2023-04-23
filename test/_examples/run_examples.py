# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import subprocess


def run_terminal_examples_for_color() -> None:
    subprocess.call("python3 ./color/foreground/full_text.py".split())
    subprocess.call("python3 ./color/foreground/custom_text.py".split())
    subprocess.call("python3 ./color/background/full_text.py".split())
    subprocess.call("python3 ./color/background/custom_text.py".split())


def run_terminal_examples_for_bright_color() -> None:
    subprocess.call("python3 ./bright_color/foreground/full_text.py".split())
    subprocess.call("python3 ./bright_color/foreground/custom_text.py".split())
    subprocess.call("python3 ./bright_color/background/full_text.py".split())
    subprocess.call("python3 ./bright_color/background/custom_text.py".split())


def run_terminal_examples_for_effect() -> None:
    subprocess.call("python3 ./effect/full_text.py".split())
    subprocess.call("python3 ./effect/full_text_with_color.py".split())
    subprocess.call("python3 ./effect/custom_text.py".split())


def run_terminal_examples_for_rgb_color() -> None:
    subprocess.call("python3 ./rgb/full_text.py".split())
    subprocess.call("python3 ./rgb/custom_text.py".split())


def run_terminal_examples_for_hsl_color() -> None:
    subprocess.call("python3 ./hsl/full_text.py".split())
    subprocess.call("python3 ./hsl/custom_text.py".split())


def run_terminal_examples_for_hex_color() -> None:
    subprocess.call("python3 ./hex/full_text.py".split())
    subprocess.call("python3 ./hex/custom_text.py".split())


def run_terminal_examples_for_general_print_method() -> None:
    subprocess.call("python3 ./general/full_text.py".split())


if __name__ == "__main__":
    run_terminal_examples_for_color()
    run_terminal_examples_for_bright_color()
    run_terminal_examples_for_effect()
    run_terminal_examples_for_rgb_color()
    run_terminal_examples_for_hsl_color()
    run_terminal_examples_for_hex_color()
    run_terminal_examples_for_general_print_method()
