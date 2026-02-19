while True:
    print("Informe valor:")

    try:
        valor = int(input())

        if 1000 <= valor <= 9999:
            break
        else:
            print("O número deve ter exatamente 4 dígitos.")
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")


milhar = valor // 1000
centena = (valor % 1000) // 100
dezena = (valor % 100) // 10
unidade = valor % 10


valor_invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar

print("O valor invertido é:", valor_invertido)
