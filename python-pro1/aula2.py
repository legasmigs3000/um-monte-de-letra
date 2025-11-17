import random
simbolos = "+-/*!&$#?=@"
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"

caracteres_permitidos = simbolos + letras_minusculas + letras_maiusculas + numeros

tamanho_senha = int(input("Digite o comprimento da senha: "))

senha = ""

for i in range(tamanho_senha):
    senha += random.choice(caracteres_permitidos)
    
print("Sua senha gerada é:", senha)


