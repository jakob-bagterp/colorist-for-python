from enum import Enum, unique


@unique
class AnsiColor(Enum):
    """ANSI color palette 0-7 to be mixed with AnsiColorSelector for foreground (30-37), background (40-47) and other combinations."""

    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7

    def __str__(self) -> str:
        return str(self.value)


@unique
class AnsiColorSelector(Enum):
    """ANSI color selector to be mixed with AnsiColor for foreground (30-37), background (40-47) and other combinations."""

    FOREGROUND = 3
    """Mix with AnsiColor to select foreground 8 colors palette: 30-37."""

    BACKGROUND = 4
    """Mix with AnsiColor to select background 8 colors palette: 40-47."""

    BRIGHT_FOREGROUND = 9
    """Mix with AnsiColor to select bright foreground 8 colors palette: 90-97."""

    BRIGHT_BACKGROUND = 10
    """Mix with AnsiColor to select bright background 8 colors palette: 100-107."""

    def __str__(self) -> str:
        return str(self.value)


@unique
class AnsiRgbColorSelector(Enum):
    """ANSI RGB color selector to be mixed with AnsiColor for foreground (30-37), background (40-47) and other combinations."""

    FOREGROUND = "38;2"
    """Parameter for RGB foreground color sequence: 38;2;r;g;b."""

    BACKGROUND = "48;2"
    """Parameter for RGB background color sequence: 48;2;r;g;b."""

    def __str__(self) -> str:
        return str(self.value)


@unique
class AnsiEffect(Enum):
    """ANSI effect codes to be mixed with effect selector."""

    RESET_ALL = 0
    BOLD = 1
    DIM = 2
    UNDERLINE = 4
    BLINK = 5

    def __str__(self) -> str:
        return str(self.value)
