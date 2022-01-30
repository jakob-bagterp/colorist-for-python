import subprocess

def run_terminal_examples() -> None:
    subprocess.call("python3 ./test/color/full_text.py".split())
    subprocess.call("python3 ./test/bright_color/full_text.py".split())
    subprocess.call("python3 ./test/effect/full_text.py".split())

def run_pytest() -> None:
    subprocess.call("pytest".split())

if __name__ == "__main__":
    run_terminal_examples()
    run_pytest()
