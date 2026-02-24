while True:
    try:


        nota1 = int(input("Informe uma nota "))
        nota2 = int(input("Informe uma segunda nota "))
        nota3 = int(input("Informe uma terceira nota "))

        if(nota1 < 0 or nota1 > 10):
            print("Valor inválido. A nota deve ser entre 0 e 10.")
        elif(nota2 < 0 or nota2 > 10):
            print("Valor inválido. A nota deve ser entre 0 e 10.")
        elif(nota3 < 0 or nota3 > 10):
            print("Valor inválido. A nota deve ser entre 0 e 10.")
        else:
            break
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")


maiorValor = max(nota1, nota2, nota3)

peso1 = 5 if nota1 == maiorValor else 2
peso2 = 5 if nota2 == maiorValor else 2
peso3 = 5 if nota3 == maiorValor else 2

mediaPonderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f"A média ponderada é: {mediaPonderada}")