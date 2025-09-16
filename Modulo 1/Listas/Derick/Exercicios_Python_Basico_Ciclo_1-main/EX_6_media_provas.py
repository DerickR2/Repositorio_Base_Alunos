from colorama import init, Fore
init(autoreset=True)

barra = "| ______________________________ |"
print(Fore.BLUE+f"{barra}")
print("| SISTEMA DE PROVAS")
print(Fore.BLUE+f"{barra}")
nome = input("| Nome do aluno: ")
nota1 = float(input("| Nota Da Primeira Prova: "))
nota2 = float(input("| Nota Da Segunda Prova: "))
nota3 = float(input("| Nota Da Terceira Prova: "))
print(Fore.BLUE+f"{barra}")
media = (nota1+nota2+nota3)/3

print(f"| Aluno: {nome}")
print(f"| Média: {media}")
if media >= 5:
    
    print("|",Fore.GREEN+f"Aprovado")
else:
    
    print("|",Fore.RED+f"| Reprovado")



print(Fore.BLUE+f"{barra}")