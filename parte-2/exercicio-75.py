def remove_da_lista(lista, numero):
    for valor in lista:
        if valor == numero:
            lista.remove(valor)

    print(len(lista))

remove_da_lista([1,2,3,4,5,6,7,5], 5)