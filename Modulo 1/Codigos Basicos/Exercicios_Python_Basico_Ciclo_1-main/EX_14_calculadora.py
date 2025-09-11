from colorama import init, Fore
init(autoreset=True)
# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
barra = f'|{30*"_"}|'
print(barra)
print("| Calculadora")
print(barra)

print("|1- Soma")
print("|2- Subtração")
print("|3- Mutiplicação")
print("|4- Divisão")
print(barra)

numero = int(input("| Escolha Uma Das Opções: "))
numero1 = int(input("| Digite O Primeiro Número: "))
numero2 = int(input("| Digite O Segundo Número: "))

if numero == 1:

    print(f"| O resultado é:{numero1+numero2:.2f}")


elif numero == 2:

    print(f"| O resultado é:{numero1-numero2:.2f}")

elif numero == 3:

    print(f"| O resultado é:{numero1*numero2:.2f}")


elif numero == 4:

    print(f"| O resultado é:{numero1/numero2:.2f}")

else:

    print("|",Fore.RED+"ERRO. Escolha Uma Opção Válida")