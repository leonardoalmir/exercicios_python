from random import shuffle
print("=========== DESAFIO 020 =============\n"
      "Um professor quer sortear a ordem de\n"
      "apresentação de trabalhos dos alunos.\n"
      "Faça um programa que leia o nome dos \n"
      "quatro aluinos e mostre a ordem sorteada.\n"
      "=====================================\n")
aluno1 = input("Digite o nome do 1° aluno(a): ")
aluno2 = input("Digite o nome do 2° aluno(a): ")
aluno3 = input("Digite o nome do 3° aluno(a): ")
aluno4 = input("Digite o nome do 4° aluno(a): ")
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("A ordem sorteada é: {}".format(lista))
