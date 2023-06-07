cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 030 ======================
Crie um programa que leia um número inteiro e mostre na 
tela se ele é PAR ou ÍMPAR.
=======================================================\n{}""".format(cinza, limpa))
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número {} é {}PAR{}!".format(num, azulClaro, limpa))
else:
    print("O número {} é {}ÍMPAR{}!".format(num, azulClaro, limpa))