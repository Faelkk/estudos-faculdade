import random

palavras = ["python", "codigo", "programacao", "desenvolvimento", "algoritmo"]

palavra_aleatoria = random.choice(palavras)

numero_tentativas = 6

letras_adivinhadas = set()

while numero_tentativas > 0 and numero_tentativas <= 6: 
    letra = input("Digite uma letra: ").lower()
    if(len(letra) != 1):
        while True:
         letra = input("Digite uma letra: ").lower()
         if len(letra) == 1 and letra.isalpha():
                break
         print("Por favor, digite apenas uma letra válida.")
    


    if letra in palavra_aleatoria:
        letras_adivinhadas.add(letra)
        print(f"Parabéns! A letra '{letra}' está na palavra.")
    else:
        numero_tentativas -= 1
        print(f"Ops! A letra '{letra}' não está na palavra. Você tem {numero_tentativas} tentativas restantes.")

    palavra_mostrada = ""

    for char in palavra_aleatoria:
        if char in letras_adivinhadas:
            palavra_mostrada += char + " "
        else:
            palavra_mostrada += "_ "

    print(palavra_mostrada.strip())

    if "_" not in palavra_mostrada:
        print("Parabéns! Você adivinhou a palavra!")
        break