# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("Escolha Uma Opção:")
print("1 - Dollar Para Real")
print("2 - Real Para Dollar")
opcao = input("Digite A Opção: ")

if opcao == "1":


    dollar = float(input("Informe a cotação atual do Dollar: "))
    real = float(input("Informe a quantidade de reais: "))
    mutiplicacao = real * dollar


    print(f"O Valor Em Reais É: R${mutiplicacao}")
elif opcao == "2":

    dollar = float(input("Informe a cotação atual do Dollar: "))
    real = float(input("Informe a quantidade de reais: "))
    mutiplicacao =float(f'{real / dollar:.2f}')


    print(f"O Valor Em Dólares É: ${mutiplicacao}")


else:

    print("Numero incorreto, tente novamente")