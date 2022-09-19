# 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = input("Digite seu nome completo: ").strip() #Strip remove espaços do inicio e do final.
# – O nome com todas as letras maiúsculas e minúsculas.

print(f"Seu nome em letras maísculas é : {nome.upper()}")
print(f"Seu nome em letras minúsculas é: {nome.lower()}")
# – Quantas letras ao todo (sem considerar espaços).

# qtd = len(nome) - nome.count(" ")
print(f'Seu nome tem ao todo: {len(nome) - nome.count(" ")} letras')
# – Quantas letras tem o primeiro nome.

print(f"Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras.")


