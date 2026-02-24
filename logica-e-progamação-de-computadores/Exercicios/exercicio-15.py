while True:
    try:
        print("Informe um valor:")
        valor1 = int(input())
        print("Informe um segundo valor:")
        valor2 = int(input())
        print("Informe um terceiro valor:")
        valor3 = int(input())
        break
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")



if valor1 > valor2:
    valor1,valor2=valor2,valor1

if(valor1 > valor3):
    valor1,valor3=valor3,valor1

if valor2 > valor3:
    valor2,valor3=valor3,valor2

print(f"Os valores em ordem crescente são: {valor1}, {valor2} e {valor3}")