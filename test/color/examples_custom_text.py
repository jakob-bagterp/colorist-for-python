from colorist import Color

if __name__ == "__main__":
    print("")
    print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")
    print("")
    print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
    print("")
    print("I want {0}red{1} color inside this paragraph".format(Color.RED, Color.OFF))
    print("")
