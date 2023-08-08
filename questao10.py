"""
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores
"""
numttele = int(input("Qual o numero total de eleitores de um municipio?"))
branc = int(input("Qual a quantidade de votos brancas?"))
nul =  int(input("Qual a quantidade de votos nulos?"))
val = int(input("Qual a quantidade de votos validados"))

n = numttele/100
t = branc/100
f = nul/100
e = val/100

print(n,"%")
print(t,"%")
print(f,"%")
print(e,"%")
