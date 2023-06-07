vermelho = '\033[;31m'
verde = '\033[;32m'
cinza = '\033[;37m'
amarelo = '\033[;33m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 044 ======================
Elabore um programa que calcule o valor a ser pago por 
um produto, considerando o seu preço normal e condição 
de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
=======================================================\n{}""".format(cinza, limpa))
print("="*20, "LOJAS DO LÉO", "="*20)
preco = float(input("Preço das compras: R$"))
print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input("Qual é a opção desejada? "))

if opcao == 1:
    print("Comprando à vista dinheiro/cheque, você obteve um desconto de 10%.")
    preco_final = preco * 0.9
    print("Sua compra de R${}{:.2f}{} vai custar R${}{:.2f}{} "
          "com essa forma de pagamento escolhida."
          .format(amarelo, preco, limpa, amarelo, preco_final, limpa))
elif opcao == 2:
    print("Comprando à vista no cartão, você obteve um desconto de 5%.")
    preco_final = preco * 0.95
    print("Sua compra de R${}{:.2f}{} vai custar R${}{:.2f}{} "
          "com essa forma de pagamento escolhida."
          .format(amarelo, preco, limpa, amarelo, preco_final, limpa))
elif opcao == 3:
    print("Comprando em 2x no cartão sua compra não terá juros!")
    preco_final = preco
    parcela = 2
    valor_parcela = preco_final / parcela
    print("Sua compra será parcelada (sem juros) em {}x de R${}{}{}."
          .format(parcela, amarelo, valor_parcela, limpa))
    print("Sua compra de R${}{:.2f}{} vai custar R${}{:.2f}{} "
          "com essa forma de pagamento escolhida."
          .format(amarelo, preco, limpa, amarelo, preco_final, limpa))
elif opcao == 4:
    parcela = int(input("Vai parcelar em quantas vezes:"))
    if parcela == 2:
        print("Comprando em 2x no cartão sua compra não terá juros!")
        preco_final = preco
        print("Sua compra de R${}{:.2f}{} vai custar R${}{:.2f}{} "
              "com essa forma de pagamento escolhida."
              .format(amarelo, preco, limpa, amarelo, preco_final, limpa))
    elif parcela == 1 or parcela == 0:
        print("Comprando à vista no cartão, você obteve um desconto de 5%.")
        preco_final = preco * 0.95
        print("Sua compra de R${}{:.2f}{} vai custar R${}{:.2f}{} "
              "com essa forma de pagamento escolhida."
              .format(amarelo, preco, limpa, amarelo, preco_final, limpa))
    elif parcela > 2:
        preco_final = preco * 1.2
        valor_parcela = preco_final / parcela
        print("Sua compra será parcelada (com juros) em {}x de R${}{}{}."
              .format(parcela, amarelo, valor_parcela, limpa))
        print("Sua compra de R${}{:.2f}{} vai custar R${}{:.2f}{} "
              "com essa forma de pagamento escolhida."
              .format(amarelo, preco, limpa, amarelo, preco_final, limpa))
    else:
        print("Essa opção não existe. Tente novamente.")
else:
    print("Essa opção não existe. Tente novamente.")