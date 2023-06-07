from datetime import date
vermelho = '\033[;31m'
cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 032 ======================
Faça um programa que leia um ano qualquer e mostre se 
ele é bissexto.
=======================================================\n{}""".format(cinza, limpa))
ano = int(input("Qual ano você quer saber se é bissexto? Para o ano atual, digite 0: "))

#PEGANDO O ANO ATUAL:
ano_atual = date.today().year

#ATRIBUINDO O ANO ATUAL À VARIAVEL ANO (somente se o usuário digitar 0)
if ano == 0:
    ano = ano_atual

#REGRA TEORICA:
# O ano tem que ser divisivel por 4 E...
# (o resto da divisão por 100 tem que ser diferente de 0 OU o resto da divisão por 400 tem ser 0)
print("{}====================== REGRAS =======================\nCONDIÇÂO OBRIGATÓRIA:".format(cinza))
print("É divisivel por 4? (tem que ser) {}".format(ano % 4 == 0))
print("AO MENOS UMA DESSAS CONDIÇÕES TEM QUE SER VERDADEIRA:")
print("O resto da divisão por 100 é 0? (não pode ser) {}".format(ano % 100 != 0))
print("È divisivel por 400? (tem que ser) {}{}".format(ano % 400 == 0, limpa))
print("{}======================================================{}".format(cinza, limpa))

#REGRA IMPLEMENTADA:
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {}{}{} é um ano bissexto!".format(azulClaro, ano, limpa))
else:
    print("O ano de {}{}{} não é um ano bissexto.".format(vermelho, ano, limpa))
