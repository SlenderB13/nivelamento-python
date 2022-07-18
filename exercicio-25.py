from operator import index, indexOf

valores = input('Digite quantos valores desejar[EX: 1,2,3,4]:')

valores = valores.split(',')

valor_para_conferir = input('Qual valor deseja conferir na lista?')

if valor_para_conferir in valores:
    print(f'{valor_para_conferir} está na posição {valores.index(valor_para_conferir)} na lista')
else:
    print('valor não está na lista')
