from random import randint
from time import sleep

pc = randint(0,5)
user = int(input("Digite um número entre 0 e 5: "))
print("PROCESSANDO...")
sleep(3)

if pc == user:
    print(f"O número sorteado foi: {pc}. Você acertou!")
else:
    print(f"O número sorteado foi: {pc}. Você errou!")
