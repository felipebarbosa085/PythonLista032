"""
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número
"""

num1 = int(input("Escreva o primeiro numero"))
num2 = int(input("Escreva o segundo numero numero"))

soma = num1 + num2
sub = num1 - num2
sub2 = num2 - num1
multi = num1*num2
div = num1/num2
rest = num1 % num2

print(soma)
print(sub)
print(sub2)
print(multi)
print(div)
print(rest)