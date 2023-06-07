from math import hypot
print("=========== DESAFIO 017 =============\n"
      "Faça um programa que leia o comprimento\n"
      "do cateto oposto e do cateto adjacente\n"
      "de um triângulo retângulo, calcule e\n"
      "mostre o comprimento da hipotenusa.\n"
      "=====================================\n")
catOposto = float(input("Digite o valor do coteto oposto: "))
catAdjacente = float(input("Digite o valor do cateto adjacente: "))
# Fazendo com a formula matematica: hipotenusa = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)
hipotenusa = hypot(catOposto, catAdjacente)
print("O comprimento da hipotenusa é: {:.2f}".format(hipotenusa))