while True:
    try:
        texto = str(input("Digite uma string: "))

        if texto.strip() == "":
            print("A string não pode ser vazia. Tente novamente.")
            break

        dif = False
        for i in range(len(texto) // 2):
            if texto[i] != texto[len(texto) - 1 - i]:
                dif = True
                break


        if dif:            
            print("A string possui caracteres diferentes.")
        else:   
            print("A string possui caracteres iguais.")
        break

    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")