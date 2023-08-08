"""
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
"""
val = float(input("Qual o valor da conta a ser paga?"))

valo = (val*10/100)+val

print("O valor a ser paga mais a taxa do garçom é", valo)