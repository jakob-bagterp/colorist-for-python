import subprocess

def run_terminal_examples_for_color() -> None:
    subprocess.call("python3 ./test/_example/color/full_text.py".split())
    subprocess.call("python3 ./test/_example/color/custom_text.py".split())
    
def run_terminal_examples_for_bright_color() -> None:
    subprocess.call("python3 ./test/_example/bright_color/full_text.py".split())
    subprocess.call("python3 ./test/_example/bright_color/custom_text.py".split())

def run_terminal_examples_for_background_color() -> None:
    subprocess.call("python3 ./test/_example/background_color/full_text.py".split())
    subprocess.call("python3 ./test/_example/background_color/custom_text.py".split())

def run_terminal_examples_for_background_bright_color() -> None:
    subprocess.call("python3 ./test/_example/background_bright_color/full_text.py".split())
    subprocess.call("python3 ./test/_example/background_bright_color/custom_text.py".split())

def run_terminal_examples_for_effect() -> None:
    subprocess.call("python3 ./test/_example/effect/full_text.py".split())
    subprocess.call("python3 ./test/_example/effect/full_text_with_color.py".split())
    subprocess.call("python3 ./test/_example/effect/custom_text.py".split())

def run_pytest() -> None:
    subprocess.call("pytest".split())

if __name__ == "__main__":
    run_terminal_examples_for_color()
    run_terminal_examples_for_bright_color()
    run_terminal_examples_for_background_color()
    run_terminal_examples_for_background_bright_color()
    run_terminal_examples_for_effect()
    run_pytest()
