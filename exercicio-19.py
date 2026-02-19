


import math


while True:
    try:


        a = int(input("Informe o a da formula "))
        b = int(input("Informe o b da formula  "))
        c = int(input("Informe o c da formula  "))

        delta = math.pow(b, 2) - 4*a*c
        if(delta < 0 or a == 0):
            print("A equação não possui raízes reais.")
            continue



        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)


        print(f"O valor de x1 é: {x1}")
        print(f"O valor de x2 é: {x2}")
 
        break
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")



