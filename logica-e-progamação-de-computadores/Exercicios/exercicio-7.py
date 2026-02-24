


import math


while True:
    print("Informe um tempo em segundos:")


    try:
        tempo = int(input())  


        break

    except ValueError:
        print("Valor inválido. Por favor, insira um número válido para o tempo em segundos.")



tempo_horas = tempo // 3600
tempo_minutos = (tempo % 3600) // 60
tempo_segundos =  ((tempo % 3600) % 60)

print("O tempo em horas é: " + str(tempo_horas))
print("O tempo em minutos é: " + str(tempo_minutos))
print("O tempo em segundos é: " + str(tempo_segundos))
6