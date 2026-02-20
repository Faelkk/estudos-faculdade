while True:
    try:
        salario = float(input("Informe o seu salário bruto: "))

        if salario <= 0:
            print("O salário deve ser um número positivo. Tente novamente.")
            continue

        if salario <= 1212.00:
            desconto_inss = salario * 0.075
        elif salario <= 2427.35:
            desconto_inss = salario * 0.09
        elif salario <= 3641.03:
            desconto_inss = salario * 0.12
        else:
            desconto_inss = salario * 0.14

        salario_inss = salario - desconto_inss

        if salario_inss < 1903.98:
            desconto_ir = 0
        elif salario_inss < 2826.65:
            desconto_ir = salario_inss * 0.075
        elif salario_inss < 3751.05:
            desconto_ir = salario_inss * 0.15
        elif salario_inss < 4664.68:
            desconto_ir = salario_inss * 0.225
        else:
            desconto_ir = salario_inss * 0.275

        salario_liquido = salario_inss - desconto_ir

        print(f"Salário líquido: R$ {salario_liquido:.2f}")
        break

    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")