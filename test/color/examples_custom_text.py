from colorist import Color

if __name__ == "__main__":
    print("")
    print(f"I want {Color.RED}red{Color.RESET} color inside this paragraph")
    print("")
    print(f"Both {Color.GREEN}green{Color.RESET} and {Color.YELLOW}yellow{Color.RESET} are nice colors")
    print("")
    print("I want {0}red{1} color inside this paragraph".format(Color.RED, Color.RESET))
    print("")
