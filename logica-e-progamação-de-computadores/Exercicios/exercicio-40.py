

for num in range(1, 101):
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i 
    print(f"O fatorial de {num} é: {fatorial}")