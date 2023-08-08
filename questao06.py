"""
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
"""

nome = input("Qual o nome do Usuario?")
sal = int(input("Qual o seu salário fixo?"))
tot = int(input("Qual o seu total de vendas?"))

total =(tot*15/100)+tot

print("Olá", nome, "o seu salário fixo é", sal, "sua comissao inteira é", total)