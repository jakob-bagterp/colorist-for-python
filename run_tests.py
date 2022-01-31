import subprocess

def run_terminal_examples_for_color() -> None:
    subprocess.call("python3 ./test/color/examples_full_text.py".split())
    subprocess.call("python3 ./test/color/examples_custom_text.py".split())
    
def run_terminal_examples_for_bright_color() -> None:
    subprocess.call("python3 ./test/bright_color/examples_full_text.py".split())
    subprocess.call("python3 ./test/bright_color/examples_custom_text.py".split())

def run_terminal_examples_for_effect() -> None:
    subprocess.call("python3 ./test/effect/examples_full_text.py".split())
    subprocess.call("python3 ./test/effect/examples_full_text_with_color.py".split())
    subprocess.call("python3 ./test/effect/examples_custom_text.py".split())

def run_terminal_examples_for_background_color() -> None:
    subprocess.call("python3 ./test/background_color/examples_full_text.py".split())
    subprocess.call("python3 ./test/background_color/examples_custom_text.py".split())

def run_terminal_examples_for_background_bright_color() -> None:
    subprocess.call("python3 ./test/background_bright_color/examples_full_text.py".split())
    subprocess.call("python3 ./test/background_bright_color/examples_custom_text.py".split())

def run_pytest() -> None:
    subprocess.call("pytest".split())

if __name__ == "__main__":
    run_terminal_examples_for_color()
    run_terminal_examples_for_bright_color()
    run_terminal_examples_for_background_color()
    run_terminal_examples_for_background_bright_color()
    run_terminal_examples_for_effect()
    run_pytest()
