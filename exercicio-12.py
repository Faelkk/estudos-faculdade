while True:
    try:
        print("Informe sua nota:")
        nota = float(input())
        break

    except ValueError:
        print("Nota inválida. Por favor, insira uma nota valida.")

if(nota >= 9 and nota <= 10):
    print("A nota é A.")
elif(nota >= 7 and nota <= 8.9): 
    print("A nota é B.")
elif(nota >= 5 and nota <= 6.9):
    print("A nota é C.")
elif(nota >= 3 and nota <= 4.9):
    print("A nota é D.")
elif(nota  <= 3):
    print("A nota é E.")
else:
    print("Valor inválido para a nota. Por favor, insira uma nota entre 0 e 10.")