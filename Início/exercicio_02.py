# 2 Receba ano de nascimento e ano atual. Calcule idade e semanas
# Entrada
anoNascimento = int(input("Digite o ano do seu nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - anoNascimento 
idadeSemanas = 4 * 12 * idade
# Saida
print(f"Sua idade atual é: {idade}")
print(f"Sua idade em semanas é: {idadeSemanas}")
