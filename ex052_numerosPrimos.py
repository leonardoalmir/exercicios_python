cinza = '\033[;37m'
azulClaro = '\033[;36m'
verde ='\033[;32m'
vermelho = '\033[;31m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 052 ======================
Faça um programa que leia um número inteiro e diga se 
ele é ou não um número primo.
=======================================================\n{}""".format(cinza, limpa))
vezes_divisoes = 0
escolha = int(input("Digite um número: "))
for cont in range(1, escolha+1):
    if escolha % cont == 0:
        vezes_divisoes += 1
        print(verde, cont, limpa, end=" ")
    else:
        print(vermelho, cont, limpa, end=" ")
print("\nO número {} foi divisível {} vezes.".format(escolha, vezes_divisoes))
if vezes_divisoes == 2:
    print("E por isso ele {}é primo{}.".format(verde, limpa))
else:
    print("E por isso ele {}não é primo{}.".format(vermelho, limpa))
