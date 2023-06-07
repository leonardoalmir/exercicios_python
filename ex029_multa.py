limpa = '\033[m'
cinza = '\033[;37m'
vermelho = '\033[;31m'
azulClaro = '\033[;36m'
amarelo = '\033[;33m'
brancFundoVermelho = '\033[7;30;41m'
print("""
{}==================== DESAFIO 029 ======================
Escreva um programa que leia a velocidade de um carro.
Se ela ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
=======================================================\n{}""".format(cinza, limpa))
veloc = float(input("Qual é a velocidade atual do carro? "))
if veloc > 80:
    multa = (veloc - 80) * 7
    print("{}MULTADO(A)!!! Você excedeu o limite permitido que é de 80Km/h \n"
          "Você deve pagar uma multa de{} R${:.2f}{}!".format(vermelho, amarelo, multa, vermelho))
print("{}Tenha um bom dia! Dirija com segurança!".format(amarelo))
