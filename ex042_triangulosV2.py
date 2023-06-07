vermelho = '\033[;31m'
verde = '\033[;32m'
cinza = '\033[;37m'
amarelo = '\033[;33m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 042 ======================
DESAFIO 35 dos triângulos, acrescentando o recurso de 
mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
=======================================================\n{}""".format(cinza, limpa))
print("-="*15)
print("Analisador de triângulos")
print("-="*15)

segmento1 = float(input("Digite o primeiro segmento: "))
segmento2 = float(input("Digite o segundo segmento: "))
segmento3 = float(input("Digite o terceiro segmento: "))
if (segmento1 < segmento2 + segmento3) and (segmento2 < segmento1 + segmento3) and (segmento3 < segmento1 + segmento2):
    if segmento1 == segmento2 and segmento2 == segmento3:
        tipo_triangulo = "EQUILÁTERO"
    elif segmento1 != segmento2 and segmento1 != segmento3 and segmento2 != segmento3:
        tipo_triangulo = "ESCALENO"
    else:
        tipo_triangulo = "ISÓSCELES"
    print("{}Os segmentos informados podem formar um trinângulo do tipo {}!{}".format(azulClaro, tipo_triangulo, limpa))
else:
    print("{}Os segmentos informados não podem formar um triângulo.{}".format(vermelho, limpa))