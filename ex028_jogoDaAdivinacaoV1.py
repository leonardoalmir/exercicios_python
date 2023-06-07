from random import randint
from time import sleep
limpa = '\033[m'
cinza = '\033[;37m'
roxo = '\033[:35m'
verde = '\033[;32m'
print("""{}
==================== DESAFIO 028 ======================
Escreva um programa que faça o computador "pensar" em
um número entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu
ou perdeu.
=======================================================\n{}""".format(cinza, limpa))
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
numPC = randint(0,5)
#print("Numero 'pensando' pelo computador: {}.".format(numPC))
numP1 = int(input("Em que número eu pensei? "))
print("Processando...")
sleep(2)
if (numPC == numP1):
    print("{}Parabéns! Você conseguiu me vencer!".format(verde))
else:
    print("{}Ganhei! Eu pensei no número {} e não no número {}. Haha!".format(roxo, numPC, numP1))
