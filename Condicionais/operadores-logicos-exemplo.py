# operadores lógicos 
# and - ambad as expressões devem retornar verdadeiras 
# or - basta apenas uma das expressões devem retornar verdadeira
# not - inverte o resultado da expressão lógica

print()
print("|****************************|")
print("|*****Operadores Lógicos*****|")
print("|********Versão 1.0**********|")
print("|****************************|")
print()

idade = int(input("Digite sua idade: "))
ingresso = input("Você tem o ingresso? s/n ")

# Conjugar com operador and 
if not(idade >= 18 or ingresso == "s") : 
    print("Seja bem-vindo à festa 🥳")
else : 
    print("Você não pode entrar na festa 😢")