


import math


while True:
    print("Informe o raio da esfera:")


    try:
        raio = float(input())  

        if raio <= 0:
            print("O raio deve ser um número positivo. Tente novamente.")
            continue

        break

    except ValueError:
        print("Valor inválido. Por favor, insira um número válido para o raio.")



pi = 3.14
area = 4 * math.pi * math.pow(raio, 2)

print("A área da superfície da esfera é: " + str(area))

