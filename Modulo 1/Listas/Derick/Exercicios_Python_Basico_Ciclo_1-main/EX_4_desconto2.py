# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("Produto: FIAT TORO")
print("Preço: 200000")
preco = 200000
porcentagem = int(input("Porcentagem De Desconto: "))
desconto = preco * (porcentagem/100)
total = preco - desconto

print(f"O FIAT TORO Com {porcentagem}% De Desconto Custará R$ {total} ")