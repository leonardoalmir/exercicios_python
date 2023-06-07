from datetime import date
vermelho = '\033[;31m'
verde = '\033[;32m'
cinza = '\033[;37m'
amarelo = '\033[;33m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 041 ======================
A Confederação Nacional de Natação precisa de um 
programa que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
=======================================================\n{}""".format(cinza, limpa))

ano_nasc = int(input("Informe o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual-ano_nasc
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    classificacao = "MIRIM"
elif idade <= 14:
    classificacao = "INFANTIL"
elif idade <= 19:
    classificacao = "JÚNIOR"
elif idade <= 25:
    classificacao = "SÊNIOR"
else:
    classificacao = "MASTER"

print("Classificação: {}{}{}.".format(azulClaro, classificacao, limpa))
