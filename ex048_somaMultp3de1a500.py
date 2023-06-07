cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 048 ======================
Faça um programa que calcule a soma entre todos os 
números impares que são múltiplos de três e que se 
encontram no intervalo de 1 até 500. 
=======================================================\n{}""".format(cinza, limpa))
contador = 0
soma = 0
for cont in range(1,501, 2):
    if cont % 3 == 0:
        #print(cont, end=",")
        contador += 1
        soma += cont
print("\nA soma de todos os {}{}{} valores que são múltiplos de três entre 1 e 500 é {}{}{}.".format(azulClaro, contador, limpa, azulClaro, soma, limpa))
