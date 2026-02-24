import matplotlib.pyplot as plt


# Função para carregar os dados do arquivo CSV
def carregarDados():

    dados = []

    try:
        with open("dados.csv", "r", encoding="utf-8") as arquivo:

            next(arquivo)

            for linha in arquivo:
                linha = linha.strip()

                if not linha:
                    continue

                partes = linha.split(",")

                if len(partes) != 8:
                    continue

                data = partes[0]
                dia, mes, ano = data.split("/")

                registro = {
                    "dia": int(dia),
                    "mes": int(mes),
                    "ano": int(ano),
                    "precipitacao": float(partes[1]),
                    "tempMax": float(partes[2]),
                    "tempMin": float(partes[3]),
                    "umidade": float(partes[6]),
                    "vento": float(partes[7])
}

                dados.append(registro)

        print("Dados carregados com sucesso!")

    except FileNotFoundError:
        print("arquivo 'dados.csv' não encontrado.")
        return []

    except ValueError:
        print("dados inválidos no arquivo.")
        return []

    return dados

## Repetindo validação para varios usos, criei uma função pra evitar isso
def lerInteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))

            if minimo is not None and valor < minimo:
                print("Valor abaixo do permitido!")
                continue

            if maximo is not None and valor > maximo:
                print("Valor acima do permitido!")
                continue

            return valor

        except ValueError:
            print("Digite apenas números!")



# Função para visualizar dados de um intervalo específico
def visualizarPeriodo(dados):
    while True:

        mesInicial = lerInteiro("Digite o mês inicial (1-12): ", 1, 12)
        anoInicial = lerInteiro("Digite o ano inicial (1961-2016): ", 1961, 2016)

        mesFinal = lerInteiro("Digite o mês final (1-12): ", 1, 12)
        anoFinal = lerInteiro("Digite o ano final (1961-2016): ", 1961, 2016)

        if (anoFinal < anoInicial) or (anoFinal == anoInicial and mesFinal < mesInicial):
            print("Período inválido! O período final é menor que o inicial.\n")
        else:
            break


       # Menu para selecionar quais dados mostrar apos informar dados iniciais
    print("\n1 - Todos os dados")
    print("2 - Apenas precipitação")
    print("3 - Apenas temperaturas")
    print("4 - Apenas umidade e vento")

    opcao = lerInteiro("Escolha uma opção: ", 1, 4)

    print(f"\nPeríodo: {mesInicial:02d}/{anoInicial} até {mesFinal:02d}/{anoFinal}")
    print("-" * 60)

    cabecalhos = {
        1: "Data       Precip   TempMax   TempMin   Umidade   Vento",
        2: "Data       Precip",
        3: "Data       TempMax   TempMin",
        4: "Data       Umidade   Vento"
    }

    print(cabecalhos[opcao])

    encontrou = False

    for registro in dados:

        ano = registro["ano"]
        mes = registro["mes"]

        dentroPeriodo = (
            (ano > anoInicial or (ano == anoInicial and mes >= mesInicial)) and
            (ano < anoFinal or (ano == anoFinal and mes <= mesFinal))
        )

        if dentroPeriodo:

            encontrou = True
            dataFormatada = f'{registro["dia"]:02d}/{mes:02d}/{ano}'


        # Mostra os dados de acordo com a opção escolhida,essa parte do codigo talvez fique um pouco complexa mas ela tem extrema importância na formatação pra visualizar os dados
            if opcao == 1:
                print(f'{dataFormatada}   {registro["precipitacao"]:.1f}   '
                      f'{registro["tempMax"]:.1f}   {registro["tempMin"]:.1f}   '
                      f'{registro["umidade"]:.1f}   {registro["vento"]:.1f}')

            elif opcao == 2:
                print(f'{dataFormatada}   {registro["precipitacao"]:.1f}')

            elif opcao == 3:
                print(f'{dataFormatada}   {registro["tempMax"]:.1f}   '
                      f'{registro["tempMin"]:.1f}')

            elif opcao == 4:
                print(f'{dataFormatada}   {registro["umidade"]:.1f}   '
                      f'{registro["vento"]:.1f}')

    if not encontrou:
        print("Nenhum dado encontrado para esse período.")


## Encontrar mes e ano mais chuvoso
def mesMaisChuvoso(dados):
    dadosMaisChuvosos = {}


    for dado in dados:
        ano = dado["ano"]
        mes = dado["mes"]
        precipitacao = dado["precipitacao"]

        chave = (ano, mes)

        if chave not in dadosMaisChuvosos:
            dadosMaisChuvosos[chave] = precipitacao
        else:
            dadosMaisChuvosos[chave] += precipitacao

    if not dadosMaisChuvosos:
        print("Nenhum dado disponível.")
        return

    itens = list(dadosMaisChuvosos.items())


    ## Inicializei com o primeiro registro pra não começar usando none, não acho uma boa pratica utilizar valor de none
    mesAnoMaior, maiorPrecipitacao = itens[0]

    ## Maior preciptacao
    for chave, total in itens:
        if total > maiorPrecipitacao:
            maiorPrecipitacao = total
            mesAnoMaior = chave

    ano, mes = mesAnoMaior
    print(f"Mês mais chuvoso: {mes:02d}/{ano}")
    print(f"Total de precipitação: {maiorPrecipitacao:.1f} mm")


## Pega dados do mes e pra cada ano cria um hasMap com as keys e o values
def calcularMediasMes(dados):

    mesEscolhido = lerInteiro("Digite o mês (1-12): ", 1, 12)

    medias = {}

    for ano in range(2006, 2017):

        soma = 0
        contador = 0

        for dado in dados:
            if dado["ano"] == ano and dado["mes"] == mesEscolhido:
                soma += dado["tempMin"]
                contador += 1

        if contador > 0:
            media = soma / contador
            medias[ano] = media
        else:
            medias[ano] = 0

    print(f"\nMédias da temperatura mínima para o mês {mesEscolhido} (2006-2016):")

    for ano, media in medias.items():
        print(f"{ano}: {media:.2f} °C")

    return medias

# Função para gerar gráfico de barras na vertical das médias usando mattpotlib
def gerarGrafico(medias):
    anos = list(medias.keys())
    valores = list(medias.values())

    plt.bar(anos, valores, color='skyblue')
    plt.title('Média da temperatura mínima por ano')
    plt.xlabel('Ano')
    plt.ylabel('Temperatura mínima (°C)')
    plt.xticks(anos) 
    plt.show()


## Calculo pra exibir Media geral, depois de pegar dados da funcao calcularMediaMes dos anos de 2006 a 2016

def mediaGeral(medias):
    total = sum(medias.values())
    quantidade = len(medias)
    if quantidade > 0:
        media = total / quantidade
        print(f"\nMédia geral da temperatura mínima no período: {media:.2f} °C")





## Função principal carrega dados e exibe menu
def principal():
    dados = carregarDados()
    opcao = 0


    ## Loop pra exibir menu validando input
    while opcao != 4:   

        print("\n===== MENU =====")
        print("1 - Visualizar intervalo")
        print("2 - Mês mais chuvoso")
        print("3 - Médias + Gráfico (2006-2016)")
        print("4 - Sair")

        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao < 1 or opcao > 4:
                    print("Opção inválida!")
                    continue
                break
            except ValueError:
                print("Digite apenas números!")

        if opcao == 1:
            visualizarPeriodo(dados)

        elif opcao == 2:
            mesMaisChuvoso(dados)

        elif opcao == 3:
               medias = calcularMediasMes(dados)
               mediaGeral(medias)
               gerarGrafico(medias)

        elif opcao == 4:
            print("Encerrando programa...")


principal()