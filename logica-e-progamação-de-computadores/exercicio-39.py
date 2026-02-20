

for num in range(1, 101):
    print(f"Divisores de {num}: ")
    d = 1
    while d <= num:
        if num % d == 0:
            print(d, "divide", num)
        d += 1 