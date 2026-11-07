# 4. Receba nome, peso e altura. Calcule IMC. 
# Entrada
nome = input("Digite seu nome: ")
peso = int(input("Informe o seu peso: "))
altura = float(input("Digite sua altura: "))
# Processamento
IMC = peso / altura 
# Saida
print(f"Olá, {nome} seu IMC é: {IMC}")