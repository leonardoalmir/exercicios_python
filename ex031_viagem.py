cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 031 ======================
Desenvolva um programa que pergunte a distância de uma 
viagem em Km. Calcule o preço da passagem, cobrando 
R$0,50 por Km para viagens de até 200Km e R$0,45 para 
viagens mais longas.
=======================================================\n{}""".format(cinza, limpa))
distancia = float(input("Qual a distância da viagem em Km? "))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print("Você fará uma viagem de {}{}Km{}.".format(azulClaro, distancia, limpa))
print("E o preço da sua passagem será de {}R${:.2f}{}.".format(azulClaro, preco, limpa))