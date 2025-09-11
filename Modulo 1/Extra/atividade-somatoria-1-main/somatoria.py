print("Por Favor Informe Os Dados Sobre Você Abaixo: ")
nome = input("Informe Seu Nome: ")
altura = float(input("Informe Sua Altura: "))
peso = float(input("Informe Seu Peso: "))

imc = peso / (altura ** 2) 

print("| Faixa de IMC        | Classificação                  |")
print("|---------------------|--------------------------------|")
print("| < 18.5              | Abaixo do peso                 |")
print("| 18.5 - 24.9         | Peso normal                    |")
print("| 25.0 - 29.9         | Sobrepeso                      |")
print("| 30.0 - 34.9         | Obesidade Grau I               |")
print("| 35.0 - 39.9         | Obesidade Grau II              |")
print("| ≥ 40.0              | Obesidade Grau III (mórbida)   |")
print("                                                        ")


print(f"Ola {nome}")
print(f"Sua Altura é: {altura:.2f}")


if imc <= 18.5:

    print("Você Esta Abaixo Do Peso")

elif imc <= 24.9:
    print("Você Esta com Peso Normal")

elif imc <= 29.9:
    print("Você esta com Sobrepeso")

elif imc <= 34.9:
    print("você Esta com Obesidade Grau I")

elif imc <= 39.9:
    print("você Esta com Obesidade Grau II")   

elif imc >= 40:
    print("você Esta com Obesidade Grau III")



