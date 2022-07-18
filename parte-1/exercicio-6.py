numeros_lista = []
numeros_tupla = ()

numeros_digitados = input('Digite quantos números aleatorios desejar, separando-os por vírgula:')

for numero in numeros_digitados.split(','):
    numeros_lista.append(numero)
    numeros_tupla = numeros_tupla + (numero,)

print('list:', numeros_lista)
print('tuple:', numeros_tupla)