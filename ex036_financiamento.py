amarelo = '\033[;33m'
cinza = '\033[;37m'
vermelho = "\033[;31m"
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 036 ======================
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o 
valor da casa, o salário do comprador e em quantos anos
ela vai pagar.
Calcule o valor da prestação mensal, sabendo que ela
não pode exceder 30% do salário ou então o empréstimo
será negado.
=======================================================\n{}""".format(cinza, limpa))
valor_casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o salário do comprador? R$"))
anos_parcela = float(input("Em quantos anos vai pagar a casa? "))

parcela_mensal = (valor_casa / anos_parcela) / 12
limite_comprador = salario / 3

print("Para uma casa no valor de R${}{:.2f}{}, parcelada em {}{:.1f}{} anos, o valor da parcela será "
      "R${}{:.2f}{}.".format(amarelo, valor_casa, limpa, azulClaro, anos_parcela, limpa,
                             amarelo, parcela_mensal, limpa))

if parcela_mensal <= limite_comprador:
    print("Seu limite sem comprometer sua renda é de R${}{:.2f}{} (30%), portanto o empréstimo está "
          "{}autorizado{}!".format(amarelo, limite_comprador, limpa, azulClaro, limpa))
else:
    print("Seu limite sem comprometer sua renda é de R${}{:.2f}{} (30%), portanto o empréstimo está "
          "{}negado{}.".format(amarelo, limite_comprador, limpa, vermelho, limpa))
