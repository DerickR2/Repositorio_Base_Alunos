from colorama import init, Fore
init(autoreset=True)
barra = f'| {30*"_"}|'
print(barra)
print("| SISTEMA DE PROVAS")
print(barra)

nome = input('|Qual O Nome Do Aluno? ')

nota1 = float(input('| Digite A Nota Da Primeira Prova '))
nota2 = float(input('| Digite A Nota Da Segunda Prova '))
nota3 = float(input('| Digite A Nota Da Terceira Prova '))

media = (nota1+nota2+nota3)/3
if media >= 5:
    
    print(Fore.GREEN+f"Aluno {nome} Aprovado")
else:
    
    print(Fore.RED+f"Aluno {nome} Reprovado")

print(barra)