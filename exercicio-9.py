while True:
    try:
        print("Informe um valor:")
        valor1 = int(input())

        print("Informe um segundo valor:")
        valor2 = int(input())

        print("Informe um terceiro valor:")
        valor3 = int(input())

        break

    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")



if valor3 > 0 and valor3 < 10:
    print("O número é maior que 0 e menor que 10.", True)
else:
    print(False)


if valor1 > 0 and valor1 < 10:
    print("O número é maior que 0 e menor que 10.", True)
else:
    print(False)


if valor2 > valor1 and valor2 > valor3:
    print("O número dois é maior que os valores 1 e 3.", True)
else:
    print(False)




if valor2 % 7 == 0:
    print("O número dois é divisível por 7.", True)
else:
    print(False)


if valor3 != 0 and valor2 % valor3 == 0:
    print("O número dois é múltiplo do valor 3.", True)
else:
    print(False)


if valor1 == valor2 and valor1 == valor3:
    print("Os três números são iguais.", True)
else:
    print(False)


if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
    print("Pelo menos dois números são iguais.", True)
else:
    print(False)


if(valor1 >= valor2 and valor1 >= valor3) : maior = valor1
elif(valor2 >= valor1 and valor2 >= valor3) : maior = valor2  
else: maior = valor3

print("O maior número é: " + str(maior))