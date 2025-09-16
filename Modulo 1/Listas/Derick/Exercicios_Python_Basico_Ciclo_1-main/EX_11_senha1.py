from colorama import init, Fore
init(autoreset=True)

senha = input("Digite A Senha: ")


if senha == "AC12":

    print(Fore.GREEN+"Senha Correta")


else:

    print(Fore.RED+"Senha Incorreta, Por Favor Tente Novamente")