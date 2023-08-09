---
tags:
    - Features
    - Tutorial
---

# Other String Formats
## How to Apply String Formatting and Concatenation
It's often easier and more readable to use [f-strings](https://peps.python.org/pep-0498/) as in the examples above, but f-strings aren't supported in some earlier versions of Python.

Instead, you can also use string formatting or concatenation:

```python
from colorist import Color

print("I want {0}red{1} color inside this paragraph".format(Color.RED, Color.OFF))
print("I want " + Color.RED + "red" + Color.OFF + " color inside this paragraph")
```

Both options appear the same in the terminal:

![Example of terminal message with red text color](../../assets/images/examples/color_custom_text_red.png)
