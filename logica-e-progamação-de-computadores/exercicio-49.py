
with open("Mocks/dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Olá!\n")
    arquivo.write("Linha 2: Testando gravação.\n")


with open("Mocks/dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo gravado no arquivo:")
print(conteudo)