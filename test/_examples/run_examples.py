# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import subprocess


def run_terminal_examples_for_color() -> None:
    subprocess.call("python3 ./foreground/color/full_text.py".split())
    subprocess.call("python3 ./foreground/color/custom_text.py".split())


def run_terminal_examples_for_bright_color() -> None:
    subprocess.call("python3 ./foreground/bright_color/full_text.py".split())
    subprocess.call("python3 ./foreground/bright_color/custom_text.py".split())


def run_terminal_examples_for_rgb_color() -> None:
    subprocess.call("python3 ./foreground/rgb/full_text.py".split())
    subprocess.call("python3 ./foreground/rgb/custom_text.py".split())


def run_terminal_examples_for_background_color() -> None:
    subprocess.call("python3 ./background/color/full_text.py".split())
    subprocess.call("python3 ./background/color/custom_text.py".split())


def run_terminal_examples_for_background_bright_color() -> None:
    subprocess.call("python3 ./background/bright_color/full_text.py".split())
    subprocess.call("python3 ./background/bright_color/custom_text.py".split())


def run_terminal_examples_for_background_rgb_color() -> None:
    subprocess.call("python3 ./background/rgb/full_text.py".split())
    subprocess.call("python3 ./background/rgb/custom_text.py".split())


def run_terminal_examples_for_effect() -> None:
    subprocess.call("python3 ./effect/full_text.py".split())
    subprocess.call("python3 ./effect/full_text_with_color.py".split())
    subprocess.call("python3 ./effect/custom_text.py".split())


if __name__ == "__main__":
    run_terminal_examples_for_color()
    run_terminal_examples_for_bright_color()
    run_terminal_examples_for_rgb_color()
    run_terminal_examples_for_background_color()
    run_terminal_examples_for_background_bright_color()
    run_terminal_examples_for_background_rgb_color()
    run_terminal_examples_for_effect()
