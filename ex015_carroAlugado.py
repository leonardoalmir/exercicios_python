print("=========== DESAFIO 015 =============\n"
      "Escreva um programa que pergunte a \n"
      "quantidade de Km percorridos por um carro\n"
      "alugado e a quantidade de dias pelos quais\n"
      "ele foi alugado. Calcule o preço a pagar,\n"
      "sabendo que o carro custa R$60 por dia e \n"
      "R$0,15 por Km rodado.\n"
      "=====================================\n")

dias = int(input("Quantos dias o carro ficou alugado? "))
kms = float(input("Quantos quilômetros foram rodados? "))
valorDiaria = 60
valorKms = 0.15
precoDias = dias * valorDiaria
precoKms = kms * valorKms
precoFinal = precoKms + precoDias

print("Foram rodados {}Km e o carro ficou alugado por {} dias,\n"
      "portanto o valor a pagar é de R${:.2f}.\nObrigado!".format(kms, dias, precoFinal))
