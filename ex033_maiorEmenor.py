vermelho = '\033[;31m'
cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 033 ======================
Faça um programa que leia três números e mostre qual é 
o maior e qual é o menor.
=======================================================\n{}""".format(cinza, limpa))

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

print("O maior valor digitado é {}{}{}.".format(azulClaro, maior,limpa))

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

print("O menor valor digitado é {}{}{}.".format(azulClaro, menor, limpa))