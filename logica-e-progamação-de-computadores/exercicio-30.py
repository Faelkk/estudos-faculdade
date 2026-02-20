while True:
    try:
        texto = str(input("Digite uma string: "))

        if texto.strip() == "":
            print("A string não pode ser vazia. Tente novamente.")
            break

        vogais = "aeiouAEIOU"
        totalVogais = 0
        for char in texto:
            if char in vogais:
                totalVogais += 1



        if totalVogais == 0:            
            print("A string não possui vogais.")
        else:   
            print(f"A string possui {totalVogais} vogais.")
        break   
        

    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")