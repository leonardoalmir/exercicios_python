print("========= DESAFIO 005 ===========")
print("Faça um programa que leia um \n"
      "número inteiro e mostre na tela \n"
      "o seu sucessor e seu antecessor.")
print("=================================\n")
numero = eval(input("Digite um número: "))
sucessor = numero + 1
antecessor = numero - 1
print("O sucessor de {} é {} e o antecessor é {}." .format(numero, sucessor, antecessor))