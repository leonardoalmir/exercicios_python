from math import sin, cos, tan, radians
print("=========== DESAFIO 018 =============\n"
      "Faça um programa que leia um ângulo\n"
      "qualquer e mostre na tela o valor do seno,\n"
      "cosseno e tangente desse ângulo.\n"
      "=====================================\n")
angulo = int(input("Digite um ângulo: "))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print("Para o ângulo de {}° o seno é {}, o cosseno é {} e a tangente é {:.1f}."
      .format(angulo, seno, cosseno, tangente))
