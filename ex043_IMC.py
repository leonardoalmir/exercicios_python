vermelho = '\033[;31m'
verde = '\033[;32m'
cinza = '\033[;37m'
amarelo = '\033[;33m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 043 ======================
Desenvolva uma lógica que leia o peso e a altura de uma 
pessoa, calcule seu Índice de Massa Corporal (IMC) e 
mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
=======================================================\n{}""".format(cinza, limpa))
peso = float(input("Informe o peso: (Kg) "))
altura = float(input("Informe a altura: (m) "))
imc = peso / (altura ** 2)
print("O Índice de Massa Corporal (IMC) dessa pessoa é: {}{:.1f}{}.".format(azulClaro, imc, limpa))
if imc < 18.5:
    status_imc = "\033[;31m"+"Abaixo do Peso"+"\033[;m"
elif imc < 25:
    status_imc = "\033[;32m"+"Peso Ideal"+"\033[;m"
elif imc < 30:
    status_imc = "\033[;33m"+"Sobrepeso"+"\033[;m"
elif imc < 40:
    status_imc = "\033[;31m"+"Obesidade"+"\033[;m"
else:
    status_imc = "\033[;31m"+"Obesidade Mórbida"+"\033[;m"
print("Essa pessoa está com o status de: {}{}{}.".format(azulClaro, status_imc, limpa))