def remove_da_lista(lista, numero):
    print('antes', lista)
    for valor in lista:
        if valor == numero:
            print('vou apagar')
            lista.remove(valor)

    print(len(lista))

remove_da_lista([1,2,3,4,5,6,7,5], 5)