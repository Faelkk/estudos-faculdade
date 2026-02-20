


import math


while True:
    print("Informe um valor:")


    try:
        valor = float(input())  

        if valor <= 0:
            print("O valor deve ser um número positivo. Tente novamente.")
            continue

        break

    except ValueError:
        print("Valor inválido. Por favor, insira um número válido para o valor.")



valor1 = math.pow(valor, 2)
valor2 = math.pow(valor, 3)
valor3 = math.pow(valor, 4)


print("O valor ao quadrado é: " + str(valor1))
print("O valor ao cubo é: " + str(valor2))
print("O valor à quarta potência é: " + str(valor3))
