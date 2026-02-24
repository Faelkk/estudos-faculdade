while True:
    try:
        texto = str(input("Digite uma string: "))

        if texto.strip() == "":
            print("A string não pode ser vazia. Tente novamente.")
            break

        palavras = texto.split()
        letrasIniciais = ""


        for palavra in palavras:
            letrasIniciais += palavra[0]

        if letrasIniciais == "":
            print("A string não possui letras iniciais.")
        else:
            print(f"A string possui {len(letrasIniciais)} letras iniciais: {letrasIniciais}")

        break
        

    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")