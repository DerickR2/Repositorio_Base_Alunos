from colorama import init, Fore
init(autoreset=True)

nota1 = int(input("DIgite A Primeira  Nota: "))
nota2 = int(input("DIgite A Segunda  Nota: "))

media = (nota1+nota2)/2



if media >= 5:

    print(f"Aluno Aprovado?{Fore.GREEN} {media>=5} ")

else:

    print(f"Aluno Aprovado?{Fore.RED} {media>=5}")
