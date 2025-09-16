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