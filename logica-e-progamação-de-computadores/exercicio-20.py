while True:
    try:


        saldoMedio = int(input("Informe o seu saldo "))

        if(saldoMedio < 499):
            limite = 0;
        if(saldoMedio >= 500 and saldoMedio < 1000): 
            limite = saldoMedio * 0.08
        if(saldoMedio >= 1000 and saldoMedio < 3000):
            limite = saldoMedio * 0.15

        print(f"O seu limite é de {limite} e o seu saldo médio é de {saldoMedio}")  
        break
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")


