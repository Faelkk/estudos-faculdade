

while True:
    try:
        anoBisexto = int(input("Informe um ano para saber se é bisexto: "))
        
        if anoBisexto < 1:
            print("Ano inválido. Por favor, insira um ano positivo.")
            continue  
        
        if (anoBisexto % 4 == 0 and anoBisexto % 100 != 0) or (anoBisexto % 400 == 0):
            print(f"O ano {anoBisexto} é bissexto.")
        else:   
            print(f"O ano {anoBisexto} não é bissexto.")
        break

    except ValueError:
        print("Jogada inválida. Informe um número entre 1 e 3.")

        