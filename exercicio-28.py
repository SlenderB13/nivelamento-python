numeros_pares = []

numeros = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
958,743, 527]

numeros.sort()

def verifica_par(numero):
    if(numero % 2 == 0 and numero <= 237):
        numeros_pares.append(numero)

for numero in numeros:
    verifica_par(numero)

print(numeros_pares)