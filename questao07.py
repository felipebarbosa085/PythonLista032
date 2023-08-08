"""
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações
"""

val = float(input("Qua o valor da compra?"))
num = float(input("Qual o numero de prestações?"))

ter = val/num
print("O valor de cada prestação a ser paga é R$",ter)
