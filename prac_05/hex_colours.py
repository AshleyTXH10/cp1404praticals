COLOUR_TO_HEX = {"absolute zero": "#0048ba", "aliceblue": "#f0f8ff", "alizarin crimson": "#e32636",
                 "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7",
                 "aqua": "#00ffff", "bleu de france": "#318ce7", "banana mania": "#fae7b5"}

for colour, hex in COLOUR_TO_HEX.items():
    print(f"{colour:3} is {hex}")

colour = input("Colour: ").strip().lower()
while colour != "":
    try:
        print(f"{colour} hex code is {COLOUR_TO_HEX[colour]}")
    except KeyError:
        print("Invalid colour!")
    colour = input("Colour: ").strip().lower()