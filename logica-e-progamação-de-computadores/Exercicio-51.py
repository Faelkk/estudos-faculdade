frases = ['Frase 1', 'Frase 2', 'Frase 3']
caracteresDeFrases = []

for frase in frases:
    lista_de_caracteres = []
    for char in frase:
        lista_de_caracteres.append(char)
    caracteresDeFrases.append(lista_de_caracteres)

print(caracteresDeFrases)