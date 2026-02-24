mesesAdicionados = {}
mesesAcimaDe33Graus = {}
nomesMeses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

while len(mesesAdicionados) < 12:

    while True:
        try:
            mes = int(input("Digite um numero de 1 ao 12 correspondente a cada mês do ano: "))
            if mes < 1 or mes > 12:
                print("Dado errado, tente novamente.")
                continue
            if mes in mesesAdicionados:
                print("Mês já informado!")
                continue
            break
        except ValueError:
            print("Digite apenas números inteiros!")

    while True:
        try:
            temperaturaMaximaDoMes = float(
                input("Digite uma temperatura em Celsius entre -60 e 50 graus: ").replace(",", ".")
            )
            if temperaturaMaximaDoMes < -60 or temperaturaMaximaDoMes > 50:
                print("Dado errado, tente novamente.")
                continue
            break
        except ValueError:
            print("Digite um número válido!")

    if temperaturaMaximaDoMes > 33:
        mesesAcimaDe33Graus[mes] = temperaturaMaximaDoMes

    mesesAdicionados[mes] = temperaturaMaximaDoMes

maiorTemp = max(mesesAdicionados.values())

mesesMaisQuentes = [
    mes for mes, temp in mesesAdicionados.items()
    if temp == maiorTemp
]

menorTemp = min(mesesAdicionados.values())

mesesMaisFrios = [
    mes for mes, temp in mesesAdicionados.items()
    if temp == menorTemp
]

media = sum(mesesAdicionados.values()) / len(mesesAdicionados)

print("\nMeses com temperatura acima de 33°C:")
for mes, temp in mesesAcimaDe33Graus.items():
    print(f"{nomesMeses[mes]}: {temp}°C")

print("\nO mês mais quente encontrado foi:")
for mes in mesesMaisQuentes:
    print(f"{nomesMeses[mes]} com {maiorTemp}°C")

print("\nO mês mais frio encontrado foi:")
for mes in mesesMaisFrios:
    print(f"{nomesMeses[mes]} com {menorTemp}°C")

print(f"\nMédia anual: {media:.2f}°C")