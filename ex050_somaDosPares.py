cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 050 ======================
Desenvolva um programa que leia seis números inteiros e 
mostre a soma apenas daqueles que forem pares. Se o 
valor digitado for ímpar, desconsidere-o.
=======================================================\n{}""".format(cinza, limpa))
soma = 0
contador = 0
for cont in range(0,6):
    numero = int(input("Digite o {}° número:".format(cont+1)))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print("A soma dos {} números pares digitados é: {}{}{}".format(contador ,azulClaro, soma, limpa))
