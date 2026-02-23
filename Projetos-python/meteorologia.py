mesesAdicionados = {}
mesesAcimaDe33Graus = {}
nomes_meses = {
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



while (len(mesesAdicionados) < 12):

    mes = int(input("Digite um numero de 1 ao 12 correspondente a cada mês do ano: "))

    while (mes < 1 or mes > 12):
        print("Dado errado, tente novamente.")
        mes = int(input("Digite um numero de 1 ao 12 correspondente a cada mês do ano: "))

    if mes in mesesAdicionados:
        print("Mês já informado!")
        continue

    temperaturaMaximaDoMes = float(input("Digite uma temperatura em Celsius entre -60 e 50 graus: ").replace(",", "."))

    while (temperaturaMaximaDoMes < -60 or temperaturaMaximaDoMes > 50):
        print("Dado errado, tente novamente.")
        temperaturaMaximaDoMes = float(input("Digite uma temperatura em Celsius entre -60 e 50 graus: "))


    if(temperaturaMaximaDoMes > 33 ):
         mesesAcimaDe33Graus[mes] = temperaturaMaximaDoMes

    
    mesesAdicionados[mes] = temperaturaMaximaDoMes


maior_temp = max(mesesAdicionados.values())

meses_mais_quentes = [
    mes for mes, temp in mesesAdicionados.items()
    if temp == maior_temp
]


menor_temp = min(mesesAdicionados.values())

meses_mais_frios = [
    mes for mes, temp in mesesAdicionados.items()
    if temp == menor_temp
]

media = sum(mesesAdicionados.values()) / len(mesesAdicionados)


print("\nMeses com temperatura acima de 33°C:")
for mes, temp in mesesAcimaDe33Graus.items():
    print(f"{nomes_meses[mes]}: {temp}°C")

print("\n O mês mais quente encontrado foi")
for mes in meses_mais_quentes:
    print(f"{nomes_meses[mes]} com {maior_temp}°C")

print("\n O mês mais frio encontrado foi:")
for mes in meses_mais_frios:
    print(f"{nomes_meses[mes]} com {menor_temp}°C")

print(f"\nMédia anual: {media:.2f}°C")