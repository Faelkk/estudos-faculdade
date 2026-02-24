while True:
    try:
        print("Informe sua altura:")
        valor1 = float(input())
        print("Informe seu genero, para mulheres digite 1 e para homens digite 2:")
        valor2 = int(input())
        break

    except ValueError:
        print("Valor inválido. Por favor, insira numeros validos.")




pesoIdealMulher = 62.1 * valor1 - 44.7
pesoIdealHomem = 72.7 * valor1 - 58

if(valor2 == 1):
    print("O peso ideal para mulheres é: " + str(pesoIdealMulher))
elif(valor2 == 2):
    print("O peso ideal para homens é: " + str(pesoIdealHomem))
else:
    print("Valor inválido para o gênero. Por favor, insira 1 para mulher ou 2 para homem.")