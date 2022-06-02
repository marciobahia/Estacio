soma_pares = 0
cont_pares = 0

for numero in range(1, 11, 1):
    if numero % 2 == 0:
        soma_pares = soma_pares + numero
        cont_pares += 1

    else:
        continue


print(f'A soma de pares foi {soma_pares} e a quantidade de foi {cont_pares}')

print(f'A média dos números pares foi {soma_pares/cont_pares}')
