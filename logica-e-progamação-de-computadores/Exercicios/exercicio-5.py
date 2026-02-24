


import math


while True:
    print("Informe uma temperatura em celsius:")


    try:
        temperatura = float(input())  


        break

    except ValueError:
        print("Valor inválido. Por favor, insira um número válido para a temperatura.")



temperatura_celsius = 5/9 * (temperatura - 32)

print("A temperatura em celsius é: " + str(temperatura_celsius))

