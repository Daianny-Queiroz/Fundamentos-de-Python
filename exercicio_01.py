# Entrada
idade = int(input("Digite a idade: "))  
# pega o texto e converte para número inteiro 
# alt + z - deixa toda a página centralizada 
# alt + l ou cls limpa o terminal 
# alt + sift + seta para baixo duplia a linha 

# Processamento 
idadeEmMeses = idade * 12 
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmMinutos = idadeEmHoras * 60

# Saída
print(f"Sua idade em meses é: {idadeEmMeses} meses 👍") 
print(f"Sua idade em dias é: {idadeEmDias} dias")
print(f"Sua idade em horas é: {idadeEmHoras} horas")
print(f"Sua idade em minutos é: {idadeEmMinutos} minutos")

