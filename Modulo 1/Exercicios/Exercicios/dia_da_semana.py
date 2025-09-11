from colorama import init, Fore
init(autoreset=True)
numero = int(input("Digite Um Numero "))

if numero == 1:

    print("Domingo")

elif numero == 2:

    print("Segunda")

elif numero == 3:

    print("Terça")

elif numero == 4:

    print("Quarta")


elif numero == 5:

    print("Quinta")

elif numero == 6:

    print("Sexta")

elif numero == 7:

    print("Sabado")


else:

    print(Fore.RED+f"Numero Incorreto")