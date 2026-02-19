import random

while True:
    try:
        jogada1 = int(input("Informe 1 Para Papel, 2 Para Tesoura ou 3 Para Pedra: "))
        
        if jogada1 < 1 or jogada1 > 3:
            print("Valor inválido para a jogada. Por favor, insira um valor entre 1 e 3.")
            continue  
        

        jogada2 = random.randint(1, 3)
        print(f"O computador escolheu: {jogada2}")

        if (jogada1 == 1 and jogada2 == 3) or (jogada1 == 2 and jogada2 == 1) or (jogada1 == 3 and jogada2 == 2):
            print("Você venceu!")
        elif jogada1 == jogada2:
            print("Empate!")
        else:
            print("Computador venceu!")
        break

    except ValueError:
        print("Jogada inválida. Informe um número entre 1 e 3.")

        