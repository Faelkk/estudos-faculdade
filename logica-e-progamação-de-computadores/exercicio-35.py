import random

n = int(input("Digite um numero: "))


if n <= 0:
        print("O numero não pode ser menor ou igual zero. Tente novamente.")
else:   
    soma = 0
    cont = 1
    while cont <= n:
    
        soma =  soma + (1/cont)

        cont =  cont +  1

    print(f"O valor de cont é: {cont},soma é: {soma}")
        