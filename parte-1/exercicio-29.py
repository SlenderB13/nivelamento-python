colors_1 = set(["White", "Black", "Red"])
colors_2 = set(["Red", "Green"])

colors = {color for color in colors_1 if color not in colors_2}
print(colors)