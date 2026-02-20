while True:
    try:

        diaDaSemana = int(input("Digite um dia da semana: "))

        if(diaDaSemana < 1 or diaDaSemana > 7):
            print("Valor inválido. O dia da semana deve ser entre 1 e 7.")

        if(diaDaSemana == 1):
            print("Domingo")
        elif(diaDaSemana == 2):
            print("Segunda-feira")
        elif(diaDaSemana == 3):
            print("Terça-feira")
        elif(diaDaSemana == 4):
            print("Quarta-feira")
        elif(diaDaSemana == 5):
            print("Quinta-feira")
        elif(diaDaSemana == 6):
            print("Sexta-feira")
        elif(diaDaSemana == 7):
            print("Sábado")
        break
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")



