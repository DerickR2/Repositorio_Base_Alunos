barra = f'|{30*"_"}|'
print(barra)
print("| Calculadora")
print(barra)

print("|1- Soma")
print("|2- Subtração")
print("|3- Mutiplicação")
print("|4- Divisão")
print(barra)

numero = int(input("Escolha Uma Das Opções: "))
numero1 = int(input("Digite O Primeiro Número: "))
numero2 = int(input("Digite O Segundo Número: "))

if numero == 1:

    print(numero1+numero2)


elif numero == 2:

    print(numero1-numero2)

elif numero == 3:

    print(numero1*numero2)


elif numero == 4:

    print(numero1/numero2)