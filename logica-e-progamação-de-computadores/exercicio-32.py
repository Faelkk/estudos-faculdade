import random

quantidadeDeHomensComMenosDe30Anos = 0
somaIdadeMaisDe3Filhos = 0
contadorMaisDe3Filhos = 0
rendaHomemMaisVelho = 0
ageHomemMaisVelho = 0
mulherComMaiorRenda = 0
mediaDeRenda = 0
somaFilhos = 0

for i in range(1, 2001):
    age = random.randint(1, 100)
    genero = random.choice(['M', 'F'])
    renda = random.randint(1000, 10000)
    numeroDeFilhos = random.randint(0, 5)

    if age < 30 and genero == 'M':
        quantidadeDeHomensComMenosDe30Anos += 1

    if numeroDeFilhos > 3:
        somaIdadeMaisDe3Filhos += age
        contadorMaisDe3Filhos += 1

    if genero == 'M' and age > ageHomemMaisVelho:
        ageHomemMaisVelho = age
        rendaHomemMaisVelho = renda

    if genero == 'F' and renda > mulherComMaiorRenda:
        mulherComMaiorRenda = renda

    mediaDeRenda += renda
    somaFilhos += numeroDeFilhos


mediaDeRenda /= 2000
mediaNumeroDeFilhos = somaFilhos / 2000

if contadorMaisDe3Filhos > 0:
    mediaDeIdade = somaIdadeMaisDe3Filhos / contadorMaisDe3Filhos
else:
    mediaDeIdade = 0

print("Quantidade de homens com menos de 30 anos:", quantidadeDeHomensComMenosDe30Anos)
print("Média de idade de quem tem mais de 3 filhos:", mediaDeIdade)
print("Renda do homem mais velho:", rendaHomemMaisVelho)
print("Renda da mulher mais rica:", mulherComMaiorRenda)
print("Média de renda:", mediaDeRenda)
print("Média número de filhos:", mediaNumeroDeFilhos)