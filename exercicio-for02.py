# 21) Faça um programa que receba 15 números inteiros e imprima na tela
# a somatória dos 15 números

total = 0

for x in range(1,16) : 
    n = int(input("Digite um número: "))
    total = total + n
print(f"Soma dos números: {total}")

