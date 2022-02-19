from colorist import Color, Effect

if __name__ == "__main__":
    print("")
    print(f"I want {Effect.UNDERLINE}underlined text{Effect.UNDERLINE_OFF} inside this paragraph")
    print("")
    print(f"I want {Effect.BOLD}emphasized text{Effect.BOLD_OFF} inside this paragraph")
    print("")
    print(f"I want both {Color.RED}colored and {Effect.BLINK}blinking{Effect.BLINK_OFF} text{Color.OFF} inside this paragraph")
    print("")
