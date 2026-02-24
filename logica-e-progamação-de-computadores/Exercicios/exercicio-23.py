while True:
    try:

        ano = int(input("Informe um ano entre 1900 e 2099: "))
       
        if ano < 1900 or ano > 2099:
                print("Valor inválido para o ano. Por favor, insira um ano entre 1900 e 2099.")
                break
        
        
        
        a = ano % 19
        b = ano % 4
        c = ano % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        dia = 22 + d + e

        if(ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076):
            dia = dia - 7

        if(dia > 31):
            dia = dia - 31
            print(f"A Páscoa no ano de {ano} será no dia {dia} de abril.")
        
        break

    except ValueError:
        print("Nota inválida. Por favor, insira uma nota valida.")

 