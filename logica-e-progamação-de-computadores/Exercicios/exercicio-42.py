import turtle
import random

t = turtle.Turtle()
t.hideturtle()
t.speed(0)



def desenhar_forca():
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    t.forward(200)
    t.backward(100)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(30)

def desenhar_cabeca():
    t.penup()
    t.goto(0, 40)
    t.pendown()
    t.circle(20)

def desenhar_corpo():
    t.penup()
    t.goto(0, 40)
    t.setheading(-90)
    t.pendown()
    t.forward(60)

def desenhar_braco_esq():
    t.penup()
    t.goto(0, 20)
    t.setheading(-150)
    t.pendown()
    t.forward(40)

def desenhar_braco_dir():
    t.penup()
    t.goto(0, 20)
    t.setheading(-30)
    t.pendown()
    t.forward(40)

def desenhar_perna_esq():
    t.penup()
    t.goto(0, -20)
    t.setheading(-150)
    t.pendown()
    t.forward(40)

def desenhar_perna_dir():
    t.penup()
    t.goto(0, -20)
    t.setheading(-30)
    t.pendown()
    t.forward(40)



palavras = ["python", "programa", "computador", "algoritmo"]
palavra = random.choice(palavras)

letras_descobertas = ["_"] * len(palavra)
erros = 0
tentativas_max = 6
letras_tentadas = set()

desenhar_forca()

while erros < tentativas_max and "_" in letras_descobertas:
    print("Palavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()

    if(letra in letras_tentadas):
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra
                letras_tentadas.add(letra)
    else:
        if letra not in letras_tentadas:
            letras_tentadas.add(letra)
            erros += 1

        if erros == 1:
            desenhar_cabeca()
        elif erros == 2:
            desenhar_corpo()
        elif erros == 3:
            desenhar_braco_esq()
        elif erros == 4:
            desenhar_braco_dir()
        elif erros == 5:
            desenhar_perna_esq()
        elif erros == 6:
            desenhar_perna_dir()
    print("Você tem", tentativas_max - erros, "tentativas restantes.")

if "_" not in letras_descobertas:
    print("Você venceu!")
else:
    print("Você perdeu! A palavra era:", palavra)

turtle.done()