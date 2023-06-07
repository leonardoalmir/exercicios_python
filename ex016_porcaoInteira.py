from math import trunc
print("=========== DESAFIO 016 =============\n"
      "Crie um programa que leia um número \n"
      "Real qualquer pelo teclado e mostre na\n"
      "tela a sua porção inteira.\n"
      "=====================================\n")
numReal = float(input("Digite qualquer número Real? "))
print("O número {} somente inteiro é: {} 😉".format(numReal, trunc(numReal)))
