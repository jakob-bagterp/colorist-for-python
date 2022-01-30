from colorist import Color, Effect

if __name__ == "__main__":
    print("")
    print(f"I want {Effect.UNDERLINE}underlined text{Effect.RESET_UNDERLINE} inside this paragraph")
    print("")
    print(f"I want {Effect.BOLD}emphasized text{Effect.RESET_BOLD} inside this paragraph")
    print("")
    print(f"I want both {Color.RED}colored and {Effect.BLINK}blinking{Effect.RESET_BLINK} text{Color.RESET} inside this paragraph")
    print("")
