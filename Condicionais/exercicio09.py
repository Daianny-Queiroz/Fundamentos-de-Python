# 9) Uma empresa decide dar aumento de 30% aos funcionários cujo salário é inferior a 500 reais. Escreva um programa que receba o salário de um funcionário e imprima o valor do salário reajustado ou uma mensagem caso o funcionário não tenha direito a aumento.

# Entrada
salario = float(input("Digite seu salário: "))

# Processamento
if salario < 500 : 
    salario = salario * 1.30
    print(f"Seu novo salário: R${salario:.2f} ")
else :
    print(f"Seu salário não tem direito a reajuste, salário: R${salario:.2f} ")

# Saída
print("Fim do programa")