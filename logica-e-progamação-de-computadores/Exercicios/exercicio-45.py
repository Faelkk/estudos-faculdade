import random

conceitosNotas = ["", "Péssimo", "Ruim", "Regular", "Bom", "Excelente"]
quantidadeVotosConceitosAtual = [0,0,0,0,0,0]

for i in range(25):
    nota = random.randint(1,5)
    quantidadeVotosConceitosAtual[nota] += 1


maiorQuantidadeVotos = max(quantidadeVotosConceitosAtual)
conceitoMaisVotado = conceitosNotas[quantidadeVotosConceitosAtual.index(maiorQuantidadeVotos)]
print("Resultados da Pesquisa de Satisfação:")
for nota, quantidade in enumerate(quantidadeVotosConceitosAtual):
    conceito = conceitosNotas[nota]
    if(nota != 0):
     print(f"Nota {nota} ({conceito}): {quantidade} votos")
print(f"O conceito mais votado foi: {conceitoMaisVotado} com {maiorQuantidadeVotos} votos.")
    
    
