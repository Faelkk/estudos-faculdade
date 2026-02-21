freq = {}

texto = input("Insira o seu texto ").strip().lower()

for letra in texto:
    if(letra not in freq):
        freq[letra] = 0
    
    freq[letra] = freq[letra] + 1

for chave in sorted(freq.keys()):
    print (chave ,"=>",freq[chave])