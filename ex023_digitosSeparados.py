print("""
=================== DESAFIO 023 =====================
Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos digitos separados.
=====================================================\n""")

numero = int(input("Digite um número de 0 a 9999: "))
print("Analisando o número {}...".format(numero))
#print("Tamanho: {}".format(len(numero) - 1))
unidade = int(numero / 1 % 10)
dezena = int(numero / 10 % 10)
centena = int(numero / 100 % 10)
milhar = int(numero / 1000 % 10)
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))

