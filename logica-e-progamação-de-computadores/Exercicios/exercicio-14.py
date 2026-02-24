while True:
    try:
        print("Informe um valor:")
        numero = int(input())

        if 1000 <= numero <= 9999:
            break
        else:
            print("O número deve ter exatamente 4 dígitos.")
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")


milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10

numero_invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar

if numero == numero_invertido:
    print("O número é igual ao seu inverso.")
else:
    print("O número NÃO é igual ao seu inverso.")
