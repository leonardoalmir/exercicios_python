print("=========== DESAFIO 013 =============\n"
      "Faça um algoritmo que leia o salário \n"
      "de um funcionário e mostre seu novo \n"
      "salário com 15% de aumento. \n"
      "=====================================\n")

salario = float(input("Qual o salário atual? "))
novoSalario = salario * 1.15
# Ou podemos usar: novoSalario = salario + (salario * 15 / 100)
print("O novo salário com 15% de aumento é R${:.2f}".format(novoSalario))