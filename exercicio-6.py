


import math


while True:
    
    

    try:
        print("Informe um valor:")
        valor1 = float(input())  
        print("Informe um segundo valor:")
        valor2= float(input())


        break

    except ValueError:
        print("Valor inválido. Por favor, insira um número válido para os valores informados.")



soma = valor1 + valor2
subtracao = valor1 - valor2
media = (valor1 + valor2) / 2
distancia = abs(valor1 - valor2)
maior = (valor1 + valor2 + abs(valor1 - valor2)) / 2
menor = (valor1 + valor2 - abs(valor1 - valor2)) / 2


print("A soma é: " + str(soma))
print("A subtração é: " + str(subtracao))
print("A média é: " + str(media))
print("A distância é: " + str(distancia))
print("O maior valor é: " + str(maior))
print("O menor valor é: " + str(menor))

