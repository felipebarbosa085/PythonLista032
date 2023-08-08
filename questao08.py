"""
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
"""
prec = int(input("Qual o preço do custo?"))
per = int(input("Qual o percentual ser acressido?"))
tot = (prec*per/100)+prec

print("O valo a ser pago é", tot)