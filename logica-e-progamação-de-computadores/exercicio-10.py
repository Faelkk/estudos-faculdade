while True:
    try:
        print("Informe um valor:")
        valor1 = int(input())

        break

    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")



if(valor1 > 0 ): 
    print("O número é positivo.", True)
elif(valor1 == 0):
    print("O número é zero.", True)
else:   
    print("O número é negativo.", False)

