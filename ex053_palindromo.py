cinza = '\033[;37m'
azulClaro = '\033[;36m'
verde ='\033[;32m'
vermelho = '\033[;31m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 053 ======================
Crie um programa que leia uma frase qualquer e diga se 
ela é um palíndromo, desconsiderando os espaços. 
Exemplos de palíndromos:
APOS A SOPA, 
A SACADA DA CASA, 
A TORRE DA DERROTA, 
O LOBO AMA O BOLO, 
ANOTARAM A DATA DA MARATONA.
=======================================================\n{}""".format(cinza, limpa))
frase = input("Digite uma palavra ou frase: ").strip()
frase = frase.upper()
print("O que foi digitado transformado em maiúsculo: (sem espaços no início e fim): {}{}{}".format(azulClaro, frase, limpa))
tamanho = len(frase)
print("O tamanho da frase digitada: {}{}{}".format(azulClaro ,tamanho, limpa))
frase_separada = frase.split()
print("A frase separada: {}{}{}".format(azulClaro, frase_separada, limpa))
junta_sem_espacos = "".join(frase_separada)
print("A frase junta sem espaços: {}{}{}".format(azulClaro, junta_sem_espacos, limpa))
tamanho_junta = len(junta_sem_espacos)
print("O tamanho da frase junta sem espaços: {}{}{}".format(azulClaro, tamanho_junta, limpa))
separado_por_letra = list(junta_sem_espacos)
print("A frase separada por caractere: {}{}{}".format(azulClaro, separado_por_letra, limpa))
frase_inversa = ""
for cont in range(tamanho_junta-1, 0-1, -1):
    #print(cont)
    frase_inversa = frase_inversa + separado_por_letra[cont]

print("Você digitou {}{}{}, invertendo fica assim: {}{}{}.".format(azulClaro, junta_sem_espacos, limpa, azulClaro, frase_inversa, limpa))
if junta_sem_espacos == frase_inversa:
    print("{}Você encontrou um palindromo!!!".format(verde))
else:
    print("{}Isso não é um palindromo.".format(vermelho))
