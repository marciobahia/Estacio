import math
import my_library

a = eval(input("entre com o coeficiente a da equação: "))
b = eval(input("entre com o coeficiente b da equação: "))
c = eval(input("entre com o coeficiente c da equação: "))

delta = my_library.calculaDelta(a, b, c)

print(f'O valor calculado do delta fopi {delta}')

# delta >0 : equação tem 2 raízes reais
# delta = 0: equação tem 1 raiz real
# delta <0: equação não tem raiz real
# raiz = (-b +- raiz_quadrada(delta))/2a

if delta >= 0:
    print("A equação tem 2 raízes reais")
    raiz1 = (-b + math.sqrt(delta))/2*a
    raiz2 = (-b - math.sqrt(delta))/2*a
    print(f'As raízes da equação são {raiz1} e {raiz2}')
elif delta == 0:
    print(f"A equação tem 1 raiz real.")
    raiz = (-b + math.sqrt(delta))/2*a
    print(f'A raiz da equação é {raiz}')
else:
    print("A equação não tem raiz real")
