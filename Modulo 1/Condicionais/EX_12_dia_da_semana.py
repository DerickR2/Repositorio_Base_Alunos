from colorama import init, Fore
init(autoreset=True)
# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print(Fore.BLACK+"# 1 - Domingo")
print(Fore.BLACK+"# 2 - Segunda")
print(Fore.BLACK+"# 3 - Terça")
print(Fore.BLACK+"# 4 - Quarta")
print(Fore.BLACK+"# 5 - Quinta")
print(Fore.BLACK+"# 6 - Sexta")
print(Fore.BLACK+"# 7 - Sabado")

numero = int(input(Fore.BLACK+"Digite um Número: "))

if numero == 1:

    print(Fore.GREEN+"Domingo")

elif numero == 2:

    print(Fore.YELLOW+"Segunda")

elif numero == 3:

    print(Fore.MAGENTA+"Terça")

elif numero == 4:

    print(Fore.BLUE+"Quarta")


elif numero == 5:

    print(Fore.LIGHTYELLOW_EX+"Quinta")

elif numero == 6:

    print(Fore.LIGHTBLUE_EX+"Sexta")

elif numero == 7:

    print(Fore.LIGHTMAGENTA_EX+"Sabado")


else:

    print(Fore.RED+f"Numero Incorreto, Por Favor Tente Novamente")