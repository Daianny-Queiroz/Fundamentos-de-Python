# 10) Elabore um programa para cálculo de preços de produtos que solicite o preço de
# compra do produto e o percentual a ser aplicado em cima desse valor para a venda.
# Calcule e exiba o preço de venda do produto. Se o percentual a ser aplicado for
# inferior a 50%, exiba uma mensagem informando ao usuário que o produto será
# vendido com uma margem muito pequena de lucro.

print("|**********************|")
print("|*****Exercício 10*****|")
print("|******Versão 1.0******|")
print("|**********************|")

# Entrada
preco = float(input("Digite o preço de compra do produto: "))
percentual = float(input("Digite o percentual para venda: "))

# Processamento
venda = preco + (preco * percentual /100)

print(f"O preço de venda é igual a R${venda:.2f} ")

# Condições
if percentual < 50 : 
    print(f"Seu produto será vendido com uma margem muito pequena de lucro - abaixo de 50% ")

# Saída
print("Fim do programa")
