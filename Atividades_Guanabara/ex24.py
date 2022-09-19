cidade = input("Digite o nome da sua cidade: ")
city = (cidade.upper().find("SANTO"))

if city == 0:
    print("O nome da sua cidade começa com SANTO")
else:
    print("O nome da sua cidade não começa com SANTO")
    

nome = input("Digite seu nome completo: ")
sobrenome = (nome.upper().find("SILVA"))

if sobrenome != -1:
    print("Você tem SILVA no nome.")
else:
    print("Não tem SILVA no seu nome.")