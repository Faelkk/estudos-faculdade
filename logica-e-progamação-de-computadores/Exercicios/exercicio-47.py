jogadores = []
count  = 1

while count <= 3:
    print(f"Jogador {count}")
    nome = input("Digite o nome do jogador: ")  
  

    pontos = int(input("Digite os pontos do jogador: "))
 
    assistencias = int(input("Digite as assistências do jogador: "))

    rebotes = int(input("Digite os rebotes do jogador: "))

    jogadores.append((nome, pontos, assistencias, rebotes))
    count =  count + 1

print(jogadores)
