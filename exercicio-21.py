while True:
    try:
        temperatura = int(input("Informe a temperatura em Celsius "))
        umidade = int(input("Informe a umidade em porcentagem "))

        if(temperatura > 30) :
            if(umidade > 60):
                print("O clima está quente e úmido.")
            else:
                print("O clima está quente.")
        else :
            if(temperatura <= 30 and temperatura >= 20):
                print("O clima está ameno.")
            else:
                if(temperatura < 20 and temperatura >= 10):
                    print("O clima está frio.") 
                else:
                    print("O clima está muito frio.")   
        break
    except ValueError:
        print("Valor inválido. Por favor, insira uma temperatura e umidade válido.")