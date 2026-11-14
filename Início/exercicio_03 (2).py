# 3. Quatro operações: solicite dois números e apresente os resultados da soma, subtração, multiplicação e divisão. Considere o segundo número diferente de zero.
# Entrada
num01 = float(input("Digite um número: "))
num02 = float(input("Digite outro número: "))
# Processamento
soma = num01 + num02
subtracao = num01 - num02
divisao = num01 / num02
multiplicacao = num01 * num02

# Saida 
print(f"A soma, subtração, divisão e multiplicação dos seus números é: {soma, subtracao, divisao, multiplicacao}")