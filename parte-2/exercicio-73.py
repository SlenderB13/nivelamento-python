numeros = [0,0,1,1,2,2,3,3,4,4,4]

numeros_filtrados = []

for numero in numeros:
    if(numero in numeros_filtrados):
        exit 
    else:
        numeros_filtrados.append(numero)

print('Numeros:', numeros)
print('Numeros filtrados', numeros_filtrados)
print('Tamanho da lista:', len(numeros_filtrados))