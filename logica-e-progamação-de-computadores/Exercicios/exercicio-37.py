n1 = int(input("Digite dois valores: "))
n2 = int(input("Digite o segundo valor: "))

if n1 <= 0 or n2 <= 0:
    print("O numero não pode ser menor ou igual zero. Tente novamente.")
else:
    if n1 > n2:
        n1, n2 = n2, n1

    valorImpares = 0

    while n1 <= n2:
        if n1 % 2 != 0:
            valorImpares += n1
        n1 += 1

    print(f"A soma é: {valorImpares}")