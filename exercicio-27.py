while True:
    try:
        ano = int(input("Informe um ano para saber se é bissexto: "))
        mes = int(input("Informe o número de um mês para saber quantos dias ele tem: "))


        if ano < 1:
            print("Ano inválido. Por favor, insira um ano positivo.")
            continue


        if mes < 1 or mes > 12:
            print("Valor inválido para o mês. Por favor, insira um valor entre 1 e 12.")
            continue

    
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            bisexto = True
            print(f"O ano {ano} é bissexto.")
        else:
            bisexto = False
            print(f"O ano {ano} não é bissexto.")

        if mes == 2:
            if bisexto:
                print("Fevereiro tem 29 dias.")
            else:
                print("Fevereiro tem 28 dias.")
        elif mes in [4, 6, 9, 11]:
            print("O mês tem 30 dias.")
        else:
            print("O mês tem 31 dias.")

        break  

    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros válidos.")