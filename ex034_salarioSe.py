verde = '\033[;32m'
cinza = '\033[;37m'
amarelo = "\033[;33m"
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 034 ======================
Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento. Para
salários superiores a R$1250,00, calcule um aumento de
10%. Para os inferiores ou iguais, o aumento é de 15%.
=======================================================\n{}""".format(cinza, limpa))

salario = float(input("Qua é o salário do funciuonário? R$"))
if salario >= 1250:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)

print("Quem ganhava {}R${:.2f}{}, passa a ganhar {}R${:.2f}{} agora.".format(amarelo, salario, limpa, verde, novo_salario, limpa))