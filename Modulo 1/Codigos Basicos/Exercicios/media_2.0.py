print("| ______________________________ |")
print("| SISTEMA DE PROVAS               ")
print("| ______________________________ |")
nome = input("| Nome Do Aluno: ")
primeira = float(input("| Nota Da Primeira Prova "))
segunda = float(input("| Nota Da Segunda Prova "))
terceira = float(input("Nota Da Terceira Prova "))
media = (f'{primeira+segunda+terceira}')/3


print("| ______________________________ |")
print(f"|Aluno:{nome} ",f" {media >= 5}| Aprovado? ")
print("| ______________________________ |")
