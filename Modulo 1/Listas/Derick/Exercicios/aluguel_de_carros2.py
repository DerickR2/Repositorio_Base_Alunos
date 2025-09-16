barra = f'| {30*"_"}|'

print(barra)
print("| 1- BMW")
print("| 2- CORVETTE")
print("| 3- MUSTANG")
print("| 4- FIAT UNO")
print(barra)
carro = int(input("Escolha Um Carro Usando O Número Dele "))
km  = float(input("Quantos Km Foram Percorridos?" ))
dias = int(input("Quantos Dias O Carro Foi Alugado "))

if carro == 1:
    diaria = 450

elif carro == 2:
    diaria = 500

elif carro == 3:
    diaria = 400

elif carro == 4:
    diaria = 2000
    
total_dias = (dias * diaria)
total_km = (km * 0.15)
valor_total = (total_dias + total_km)

print(f'Você Andou {km}Km Por {dias}Dias, Então O Preço A Pagar É R${valor_total}')