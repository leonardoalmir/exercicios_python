verde = '\033[;32m'
cinza = '\033[;37m'
vermelho = "\033[;31m"
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 035 ======================
Desenvolva um programa que leia o comprimento de três 
retas e diga ao usuário se elas podem ou não formar um 
triângulo.
=======================================================\n{}""".format(cinza, limpa))

print("-="*15)
print("Analisador de triângulos")
print("-="*15)

segmento1 = float(input("Digite o primeiro segmento: "))
segmento2 = float(input("Digite o segundo segmento: "))
segmento3 = float(input("Digite o terceiro segmento: "))
if (segmento1 < segmento2 + segmento3) and (segmento2 < segmento1 + segmento3) and (segmento3 < segmento1 + segmento2):
    print("{}Os segmentos informados podem formar um trinângulo!{}".format(azulClaro, limpa))
else:
    print("{}Os segmentos informados não podem formar um triângulo.{}".format(vermelho, limpa))
