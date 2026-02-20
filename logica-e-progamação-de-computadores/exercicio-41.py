

from random import random


intervalo1 = 0,25
intervalo2 = 26,50
intervalo3 = 51,75
intervalo4 = 76,100
countIntervalo1 = 0
countIntervalo2 = 0
countIntervalo3 = 0
countIntervalo4 = 0

while True:
    print("Digite um numero inteiro positivo")
    n = int(input())
    if n <= 0:
        print("Numero negativo não permitido, tente novamente")
        break

    if n >= 1 and n <= 25:
            countIntervalo1 += 1
    elif n >= 26 and n <= 50:
            countIntervalo2 += 1
    elif n >= 51 and n <= 75:
            countIntervalo3 += 1
    elif n >= 76 and n <= 100:
            countIntervalo4 += 1


print(f"Quantidade de numeros no intervalo {intervalo1}: {countIntervalo1}")
print(f"Quantidade de numeros no intervalo {intervalo2}: {countIntervalo2}")    
print(f"Quantidade de numeros no intervalo {intervalo3}: {countIntervalo3}")
print(f"Quantidade de numeros no intervalo {intervalo4}: {countIntervalo4}")