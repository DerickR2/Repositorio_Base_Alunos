dias = int(input('Por Quantos Dias O Carro Foi Alugado? '))
km = float(input('Por Quantos Km O Carro Rodou? '))

total_dias = (dias * 60)
total_km = (km * 0.15)
valor_total = (total_dias + total_km)

print(f'Você Andou {total_km}Km Por {dias}Dias, Então O Preço A Pagar É R${valor_total}')