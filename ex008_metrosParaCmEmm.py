print("=========== DESAFIO 008 =============")
print("Escreva um programa que leia um \n"
      "valor em metros e o exiba convertido \n"
      "em centimetros e milimetros.")
print("=====================================\n")
valorMetros = eval(input("Digite um valor em metros: "))
centimetros = valorMetros * 100
milimetros = valorMetros * 1000
print("{}m convertido é igual a {}cm e {}mm".format(valorMetros, centimetros, milimetros))
