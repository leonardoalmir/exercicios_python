cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 047 ======================
Crie um programa que mostre na tela todos os números 
pares que estão no intervalo entre 1 e 50.
=======================================================\n{}""".format(cinza, limpa))
for cont in range(2, 51, 2):
    print(cont, end=" ")
print(azulClaro+"Acabou")
