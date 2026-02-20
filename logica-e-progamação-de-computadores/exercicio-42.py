

from random import random


quantidadeMulheresSalarioMenor3500 = 0
maiorIdade = 0
menorIdade = 0
quantidadeDePessoas = 0
quantidadeMulheresSalarioMenor3500 = 0
mediaSalario = 0


while True:
    print("Digite uma idade, para nao continuar digite uma idade menor que 0")
    idade = int(input())
    if idade < 0:
        print("Idade inválida, tente novamente")
        break

    

    if idade > maiorIdade:
        maiorIdade = idade
    if menorIdade == 0 or idade < menorIdade:
        menorIdade = idade

    quantidadeDePessoas += 1
    print("Digite a quantia do salario")
    salario = float(input())
    if salario < 0:
        while salario < 0:
            print("Salário inválido, tente novamente")
            salario = float(input())
    
    mediaSalario += salario / quantidadeDePessoas

    print("Digite 1 para sexo Feminino ou 2 para sexo Masculino")
    sexo = int(input())
    if sexo != 1 and sexo != 2:
        while sexo != 1 and sexo != 2:
            print("Sexo inválido, tente novamente")
            sexo = int(input())
    

    if(sexo == 1 and salario < 3500):
        quantidadeMulheresSalarioMenor3500 += 1



   

    print(f"Quantidade de pessoas cadastradas no momento é : {quantidadeDePessoas}")
    print(f"Quantidade de mulheres com salario menor que 3500 no momento é : {quantidadeMulheresSalarioMenor3500}")
    print(f"Media salarial no momento é : {mediaSalario}")
    print(f"Maior idade no momento é : {maiorIdade}")
    print(f"Menor idade no momento é : {menorIdade}")

