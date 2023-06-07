from time import sleep

vermelho = '\033[;31m'
verde = '\033[;32m'
cinza = '\033[;37m'
amarelo = '\033[;33m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 046 ======================
Faça um programa que mostre na tela uma contagem 
regressiva para o estouro de fogos de artifício, indo 
de 10 até 0, com uma pausa de 1 segundo entre eles.
=======================================================\n{}""".format(cinza, limpa))
print("=-" * 11)
print("Contagem regressiva!!!")
print("-=" * 11)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(azulClaro, "Buum", amarelo, "BUUMMM",verde, "POOOWW!!!", limpa)