# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

barra = ("| ------------------------------ |")
print(barra)
print("| ---------- CADASTRO ---------- |")
print(barra)
nome = input("| Nome: ")
idade = int(input("| Idade: "))
email = input("| Email: ")
Senha = input("| Senha: ")

print("                                  ")
print(barra)
print("| ----- USUÁRIO CADASTRADO ----- |")
print(f"| Seja bem vindo(a): {nome}")
print(f"| Email: {email}")
print(f"| Idade: {idade}")
print(barra)