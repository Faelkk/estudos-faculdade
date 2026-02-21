with open("Mocks/Altura.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines() 

for linha in linhas:
    linha = linha.strip()  
    nome, altura = linha.split("-") 
    print(f"{nome.strip()} tem {altura.strip()} m de altura.")