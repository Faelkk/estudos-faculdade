valorIsPerfeito = int(input("Digite um valor para verificar se é perfeito: "))

if valorIsPerfeito <= 0:
    print("O numero não pode ser menor ou igual zero. Tente novamente.")
else:

    divores = []
    valorSomaDivores = 0
    n1 = 1
    while n1 < valorIsPerfeito:
        if valorIsPerfeito % n1 == 0:
            divores.append(n1)
            valorSomaDivores += n1
        n1 += 1

    print(f"A soma é: {valorSomaDivores}")
    if valorSomaDivores == valorIsPerfeito:
        print("O número é perfeito.")
    else:
        print("O número não é perfeito.")