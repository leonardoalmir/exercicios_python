print("=========== DESAFIO 012 =============\n"
      "Faça um algoritmo que leia o preço \n"
      "de um produto e mostre seu novo preço \n"
      "com 5% de desconto. \n"
      "=====================================\n")
preco = float(input("Qual o valor do produto? "))
precoDesconto = preco - (preco * 0.05)
print("O novo preço com um desconto de 5% é R${:.2f}.".format(precoDesconto))

