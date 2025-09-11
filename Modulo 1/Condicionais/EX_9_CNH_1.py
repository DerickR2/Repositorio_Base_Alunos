from colorama import init, Fore
init(autoreset=True)
# Escreva um programa simples que pede a idade do usuário e 
# depois mostre na tela com valor BOOLEANO (True ou False) se o usuário pode tirar a CNH (Carteira Nacional de Habilitação) ou não.
# Para tirar carteira no Brasil, a idade mínima é 18 anos.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite sua idade: 19
# Pode tirar carteira de motorista? True

# Exemplo 2:
# Digite sua idade: 17
# Pode tirar carteira de motorista? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

idade = int(input("Digite Sua Idade: "))
cnh = idade >= 18

if cnh:
    print(f"Pode Tirar Sua Carteira De Motorista?{Fore.GREEN} {cnh} ")

else:

    print(f"Pode Tirar Sua Carteira De Motorista?{Fore.RED} {cnh} ")