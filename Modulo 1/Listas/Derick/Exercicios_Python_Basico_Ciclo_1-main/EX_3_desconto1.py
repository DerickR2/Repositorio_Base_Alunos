# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

preco = float(input("Qual O Preço Do Produto? "))
porcentagem = int(input('Qual A Porsentagem De Desconto? '))
desconto = preco * (porcentagem/100)
print(f"O Produto Que Custa R${preco} Agora Terá {desconto}R$ De Desconto")