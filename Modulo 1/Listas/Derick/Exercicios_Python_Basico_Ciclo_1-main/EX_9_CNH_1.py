from colorama import init, Fore
init(autoreset=True)

idade = int(input("Digite Sua Idade: "))
cnh = idade >= 18

if cnh:
    print(f"Pode Tirar Sua Carteira De Motorista?{Fore.GREEN} {cnh} ")

else:

    print(f"Pode Tirar Sua Carteira De Motorista?{Fore.RED} {cnh} ")