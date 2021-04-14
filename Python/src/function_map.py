lista = [1, 2, 3, 4, 5]


def multiplica(item):
    return item*3


nova_lista = map(multiplica, lista)
print(list(nova_lista))
