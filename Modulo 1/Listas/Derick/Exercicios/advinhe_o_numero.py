from random import randint

numero = randint(1,10)
numero1 = int(input("Qual É O Número Que Eu Estou Pensando: "))

while numero != numero1 :
    print("Número Errado, Tente Denovo")
    numero1 = int(input("Qual É O Número Que Eu Estou Pensando: "))
print("Acertou O Número")