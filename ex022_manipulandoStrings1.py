print("""=================== DESAFIO 022 =====================
Crie um programa que leia o nome completo de
uma pessoa e mostre:

1 - O nome com todas as letras em maiúsculas.
2 - O nome com todas as letras em minúsculas.
3 - Quantas letras ao todo (sem considerar espaços).
4 - Quantas letras tem o primeiro nome.
=====================================================\n""")


nome = input("Digite um nome completo: ")
print("Analisando nome...")
print("Maiúsculas: {}".format(nome.upper()))
print("Minúsculas: {}".format(nome.lower()))
print("Total de letras (sem espaços): {}".format(len(nome) - nome.count(" ")))
primeiroNome = nome.split()
print("Total de letras no primeiro nome: {} ({} letras).".format(primeiroNome[0], len(primeiroNome[0])))