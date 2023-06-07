print("=========== DESAFIO 010 =============\n"
      "Crie um programa que leia quanto \n"
      "dinheiro uma pessoa tem na carteira \n"
      "e mostre quantos dólares ela pode \n"
      "comprar.")
print("=====================================\n")
dolar = 3.27
dinheiroCarteira = float(input("Quando de dinheiro você tem na carteira em R$? "))
print("Com R${} você pode comprar US${:.2f}.".format(dinheiroCarteira, (dinheiroCarteira/dolar)))