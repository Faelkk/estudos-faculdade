while True:
    try:
        print("Informe a hora de inicio:")
        hora = int(input())
        print("Informe os minutos de inicio:")
        minutos = int(input())
        print("Informe a hora de termino:")
        hora_termino = int(input())
        print("Informe os minutos de fim:")
        minutos_termino = int(input())
        break
    except ValueError:
        print("Horario inválido. Por favor, insira uma hora valida.")


inicio_total = hora * 60 + minutos
fim_total = hora_termino * 60 + minutos_termino

duracao = fim_total - inicio_total


if duracao < 0:
    duracao += 24 * 60


if duracao > 24 * 60:
    print("Valor inválido para duração. O horário máximo é de 24 horas.")
else:
    horas = duracao // 60
    minutos = duracao % 60
    print(f"Duração do jogo foi: {horas} horas e {minutos} minutos")
