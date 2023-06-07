from datetime import date

amarelo = '\033[;33m'
cinza = '\033[;37m'
vermelho = "\033[;31m"
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 039 ======================
Faça um programa que leia o ano de nascimento de um 
jovem e informe, de acordo com a sua idade, se ele ainda 
vai se alistar ao serviço militar, se é a hora exata de 
se alistar ou se já passou do tempo do alistamento. Seu 
programa também deverá mostrar o tempo que falta ou que 
passou do prazo.
=======================================================\n{}""".format(cinza, limpa))
ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
ano_alistamento = ano_nasc + 18
print("Você tem {} anos agora em {}.".format(idade,ano_atual))
if idade < 18:
    faltam = 18 - idade
    print("Ainda falta(m) {} ano(s) para o seu alistamento, "
     "que {}será em {}{}.".format(faltam, azulClaro, ano_alistamento, limpa))
elif idade == 18:
    print("{}Você deve se alistar imediatamente!!!{}".format(amarelo, limpa))
else:
    print("{}Já deveria ter se alistado há {} anos.\n"
          "Seu alistamento foi em {}.{}\n"
          .format(vermelho, ano_atual-ano_alistamento, ano_alistamento, limpa))