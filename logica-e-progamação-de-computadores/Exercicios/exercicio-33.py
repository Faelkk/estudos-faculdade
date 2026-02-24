import random


while True:
    try:
        random_number = random.randint(1, 100)

        for i in range(1,11):
            palpite = int(input("Digite um número entre 1 e 100: "))
            if palpite == random_number:
                print("Parabéns! Você acertou o número.")
                break
            if(palpite < random_number):
                print("O número é maior do que o seu palpite."  )
            elif(palpite > random_number):
                print("O número é menor do que o seu palpite."  )
        else:
            print("Você errou o número.", "O número correto era:", random_number)

        break
        

    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")