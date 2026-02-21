def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
    print()  

def checar_vitoria(tabuleiro, jogador):

    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):  
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)): 
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:  
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:  
        return True
    return False

def jogoDaVelha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        

        try:
            linha = int(input("Escolha a linha (0-2): "))
            coluna = int(input("Escolha a coluna (0-2): "))
        except ValueError:
            print("Digite apenas números!")
            continue

   
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Posição inválida! Tente novamente.")
            continue
        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada! Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if checar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break


        if jogadas == 9:
            imprimir_tabuleiro(tabuleiro)
            print("Empate! Ninguém venceu.")
            break


        jogador_atual = "O" if jogador_atual == "X" else "X"


while True:
    print("1- Jogar")
    print("2- Sair")

    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas 1 ou 2")
        continue

    while op != 1 and op != 2:
        op = int(input("Escolha inválida, selecione novamente (1 ou 2): "))

    if op == 2:
        print("Fim do programa")
        break
    else:
        jogoDaVelha()