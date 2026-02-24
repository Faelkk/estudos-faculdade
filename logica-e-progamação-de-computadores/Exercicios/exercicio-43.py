import turtle

def quadrado(t, tamanho):
    for _ in range(4):
        t.forward(tamanho)
        t.left(90)

def porta(t, largura, altura):
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.forward(largura)
    t.right(90)
    t.forward(altura)
    t.left(90)

def casa(t, x, y, tamanho):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    quadrado(t, tamanho)

 
    t.penup()
    t.goto(x, y + tamanho)
    t.setheading(0)
    t.pendown()

    t.forward(tamanho)
    t.left(135)
    t.forward(tamanho * 0.707)
    t.left(90)
    t.forward(tamanho * 0.707)


    largura_porta = tamanho * 0.25
    altura_porta = tamanho * 0.5

    t.penup()
    t.goto(x + (tamanho - largura_porta)/2, y)
    t.setheading(0)
    t.pendown()

    porta(t, largura_porta, altura_porta)



t = turtle.Turtle()
t.speed(0)

casa(t, -200, -100, 120)
casa(t, 50, -100, 150)

turtle.done()