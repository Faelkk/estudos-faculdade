import random

mediaIdades = 0
maiorIdade = 0
menorIdade = 100
for i in range(1,21):
    idade = random.randint(1,100)
    print(f"Idade {i}: {idade}")
    mediaIdades += idade / 20

    if(idade > maiorIdade):
        maiorIdade = idade
    if(idade < menorIdade):
        menorIdade = idade

    
print(f"A média das idades é: {mediaIdades:.2f}")
print(f"A maior idade é: {maiorIdade}")
print(f"A menor idade é: {menorIdade}")