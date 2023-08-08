"""
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores
"""
numttele = int(input("Qual o numero total de eleitores de um municipio?"))
branc = int(input("Qual a quantidade de votos brancas?"))
nul =  int(input("Qual a quantidade de votos nulos?"))
val = int(input("Qual a quantidade de votos validados"))

n = numttele/branc*100
t = numttele/nul*100
f = numttele/val*100

print("Resultados das eleições:")
print("O valor de votos brancos é",n,"%")
print("O valor de votos nulos é",t,"%")
print("O valor de votos validados é",f,"%")

