#17 - Faça um programa que leia o comprimento do cateto oposto de
# um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt, hypot

cat_op = float(input("Cateto oposto: "))
cat_adj = float(input("Cateto adjacente: "))

# primeira forma importando hypot
hip2 = hypot(cat_op,cat_adj )
print(f"Hipotenusa = {hip2:.2f}")

#segunda forma usando sqrt
hip = sqrt(cat_op**2 + cat_adj**2)
print(f"Hipotenusa = {hip:.2f}")
# _______________________________________________________________________
# 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print(f"O ângulo de {angulo} tem o seno = {seno:.2f}, cosseno = {coss:.2f} e tangente = {tang:.2f} ")
 