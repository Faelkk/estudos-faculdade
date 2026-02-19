while True:
    try:

        unitario = int(input("Digite o valor unitario: "))

        if(unitario < 0):
            print("Valor inválido. O valor unitário deve ser positivo.")
        break
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")



if(unitario < 10): 
    valorVenda = unitario * 1.7

if(unitario >= 10 and unitario <= 29):
    valorVenda = unitario * 1.5


if(unitario >= 30 and unitario <= 49):
    valorVenda = unitario * 1.4

if(unitario >= 50):
    valorVenda = unitario * 1.3

print("Valor de venda: ", valorVenda)
