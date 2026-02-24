import random

valor = int(input("Digite um valor: "))


while True:
    if valor == 0:
        print("O valor não pode ser zero. Tente novamente.")
        break

    if valor % valor == 0 and valor % 1 == 0:
        print(f"O valor {valor} é um número primo.")
    else:
        print(f"O valor {valor} não é um número primo.")
    
    break