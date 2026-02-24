import random
vendas = 50

vendas = 50

tamanhos = ("P", "M", "G")
cores = ("Branco", "Preto", "Azul")

contagem_tamanhos = {"P": 0, "M": 0, "G": 0}
contagem_cores = {"Branco": 0, "Preto": 0, "Azul": 0}

for _ in range(vendas):
    tamanho_sorteado = random.choice(tamanhos)
    cor_sorteada = random.choice(cores)

    contagem_tamanhos[tamanho_sorteado] += 1
    contagem_cores[cor_sorteada] += 1

tamanho_preferido = max(contagem_tamanhos, key=contagem_tamanhos.get)
cor_preferida = max(contagem_cores, key=contagem_cores.get)

print("A cor preferida é:", cor_preferida)
print("Quantidade de peças vendidas do tamanho M:", contagem_tamanhos["M"])
print("Tamanho preferido:", tamanho_preferido)
    
    