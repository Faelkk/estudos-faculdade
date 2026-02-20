while True:
    try:

        presença = float(input("Informe sua presença nas aulas (entre 0 e 100): "))
        nota1 = float(input("Informe sua nota na primeira prova (entre 0 e 10): "))
        nota2 = float(input("Informe sua nota na segunda prova (entre 0 e 10): "))
        nota3 = float(input("Informe sua nota na terceira prova (entre 0 e 10): "))
    
        if presença < 0 or presença > 100:
                print("Valor inválido para a presença. Por favor, insira uma presença entre 0 e 100.")
                break
        if presença < 75:
                print("Aluno reprovado automaticamente por falta.")    
                break
        if nota1 < 0 or nota1 > 10:
                print("Valor inválido para a nota. Por favor, insira uma nota entre 0 e 10.")
                break
        if nota2 < 0 or nota2 > 10:
                print("Valor inválido para a nota. Por favor, insira uma nota entre 0 e 10.")
                break
        if nota3 < 0 or nota3 > 10:
                print("Valor inválido para a nota. Por favor, insira uma nota entre 0 e 10.")
                break
        
        
        grauG1 = (nota1 + nota2 + nota3) / 3

        if(grauG1 >= 7):
            print("Aluno aprovado.")
        if(grauG1 >= 4 and grauG1 < 7):
            print("Aluno em recuperação.")
            notaRp = float(input("Informe sua nota na prova de recuperação (entre 0 e 10): "))
            if (notaRp + grauG1) / 2 >= 5:
                print("Aluno aprovado na recuperação.")
            else:
                print("Aluno reprovado na recuperação.")
        if(grauG1 < 3.9):
            print("Aluno reprovado por nota.")

        break

    except ValueError:
        print("Nota inválida. Por favor, insira uma nota valida.")

