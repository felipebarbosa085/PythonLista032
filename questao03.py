"""
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
"""

peso = float(input("Qual o seu peso em (kg)?"))
alt = float(input("Qual a sua altura em (m)? "))

pesoo = peso*1000

alto = alt*100

print("Voce tem um peso em gramas de", pesoo, "e a sua altura em cm é ", alto)