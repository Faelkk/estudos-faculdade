n = int(input("Digite quantos termos você quer somar: "))

if n <= 0:
    print("O numero não pode ser menor ou igual zero. Tente novamente.")
else:
    soma = 0
    numerador = 2
    denominador = 1
    contador = 0

    while contador < n:
        soma += numerador / denominador
        numerador += 2
        denominador += 2
        contador += 1

    print(f"A soma é: {soma}")