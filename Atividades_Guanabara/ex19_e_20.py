# 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice, shuffle
al1 = input("Primeiro Aluno(a): ")
al2 = input("Segundo Aluno(a): ")
al3 = input("Terceiro Aluno(a): ")
al4 = input("Quarto Aluno(a): ")

lista = [al1,al2, al3, al4]
sorteado = choice(lista)
print(f"O Aluno(a) sorteado é: {sorteado}")
#_________________________________________________________________________________
# 20 - Ele também quer sortear a ordem de apresentação dos alunos. Faça um programa
 # que leia o nome dos quatro alunos e mostre a ordem sorteada.
shuffle(lista) #embaralhar
print(f"A ordem de apresentação será: \n{lista}")