"""
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
"""
anos = int(input("Digite o numero dos seus anos?"))
meses = int(input("Digite o numero dos seus meses?"))
dias = int(input("Digite o numero dos seus dias ?"))

h = (anos*365)+(meses*30)+dias


print("A sua idade contada em dias é", h)