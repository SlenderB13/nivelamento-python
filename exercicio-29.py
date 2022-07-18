cores_1 = set(["White", "Black", "Red"])
cores_2 = set(["Red", "Green"])
cores_ausentes = []

for cor in cores_1:
    if cor not in cores_2:
        cores_ausentes.append(cor)

print(cores_ausentes)