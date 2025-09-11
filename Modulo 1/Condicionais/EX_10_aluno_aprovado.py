from colorama import init, Fore
init(autoreset=True)
# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nota1 = int(input("DIgite A Primeira  Nota: "))
nota2 = int(input("DIgite A Segunda  Nota: "))

media = (nota1+nota2)/2



if media >= 5:

    print(f"Aluno Aprovado?{Fore.GREEN} {media>=5} ")

else:

    print(f"Aluno Aprovado?{Fore.RED} {media>=5}")
