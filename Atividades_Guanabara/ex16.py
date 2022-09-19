
# 16 - Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção inteira.
from math import trunc, sqrt, hypot

num = float(input("Digite um número: "))
print(f"O número foi {num} e a sua porção inteira é: {trunc(num)}")

# segunda forma de resolver usando uma função interna (int)
print(f"O número foi {num} e a sua porção inteira é: {int(num)}")

