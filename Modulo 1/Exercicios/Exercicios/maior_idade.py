from colorama import init, Fore
init(autoreset=True)
idade = int(input('Quantos Anos Vc Tem? '))


if idade >= 18:
    
    print(Fore.GREEN+f"Maior De Idade")
else:
    
    print(Fore.RED+f"Menor De Idade")