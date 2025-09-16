carro = input('Qual Foi O Modelo Do Carro Alugado: ')
dias = input("Por Quantos Dias O Carro Foi Alugado: ")
km = input('Quantos Km O Carro Rodou: ')

if carro == 'uno':
     diaria = 40

elif carro == 'bmw':
    diaria = 1000

else:
    diaria = 60

valor_dia = 0.25
dias = int(dias)
km = float(km)

valor_dias = dias * diaria
valor_km = km * 0.15
valor_total = valor_dias + valor_km



print(f"Você Andou {km}Km Por {dias} Dias, Então O Preço A Pagar É R${valor_total:.2f}")
