print("=========== DESAFIO 011 =============\n"
      "Faça um programa que leia a largura \n"
      "e a altura de uma parede em metros, \n"
      "calcule a sua área e a quantidade de \n"
      "tinta necessária para pintá-la, \n"
      "sabendo que cada litro de tinta, \n"
      "pinta uma área de 2m2. \n"
      "=====================================\n")
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
quantTinta = area / 2
print("A área dessa parede são {}m2 ".format(area), end="")
print("e você precisará de {}L de tinta para pintá-la".format(quantTinta))