"""
Hex Colours
Estimate: 20 minutes
Actual:   30 minutes
"""
COLOR_CODES = {"ARYLIDE YELLOW": "#e9d66b", "BABY PINK": "#f4c2c2", "AQUA": "#00ffff", "BRIGHT GREEN": "66ff00",
               "AZURE": "#f0ffff", "BEIGE": "#f5f5dc", "WHITE": "#ffffff", "BLACK": "#000000",
               "BARN RED": "#7c0a02", "BLUE": "#0000ff"}

while True:
    color_name = input("Enter a color name (or blank to stop): ").upper()

    if color_name == "":
        break

    try:
        color_code = COLOR_CODES[color_name]
        print(f"The hexadecimal color code for {color_name} is {color_code}")
    except KeyError:
        print("Invalid color name")

