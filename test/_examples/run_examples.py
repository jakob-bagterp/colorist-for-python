import subprocess


def run_terminal_examples_for_color() -> None:
    subprocess.call("python3 ./color/full_text.py".split())
    subprocess.call("python3 ./color/custom_text.py".split())


def run_terminal_examples_for_bright_color() -> None:
    subprocess.call("python3 ./bright_color/full_text.py".split())
    subprocess.call("python3 ./bright_color/custom_text.py".split())


def run_terminal_examples_for_background_color() -> None:
    subprocess.call("python3 ./background_color/full_text.py".split())
    subprocess.call("python3 ./background_color/custom_text.py".split())


def run_terminal_examples_for_background_bright_color() -> None:
    subprocess.call("python3 ./background_bright_color/full_text.py".split())
    subprocess.call("python3 ./background_bright_color/custom_text.py".split())


def run_terminal_examples_for_effect() -> None:
    subprocess.call("python3 ./effect/full_text.py".split())
    subprocess.call("python3 ./effect/full_text_with_color.py".split())
    subprocess.call("python3 ./effect/custom_text.py".split())


if __name__ == "__main__":
    run_terminal_examples_for_color()
    run_terminal_examples_for_bright_color()
    run_terminal_examples_for_background_color()
    run_terminal_examples_for_background_bright_color()
    run_terminal_examples_for_effect()
