from random import choice
print("=========== DESAFIO 019 =============\n"
      "Um professor quer sortear um dos seus\n"
      "quatro alunos para apagar o quadro.\n"
      "Faça um programa que ajude ele, lendo\n"
      "o nome des e escrevendo o nome do\n"
      "escolhido.\n"
      "=====================================\n")
aluno1 = input("Digite o nome do 1° aluno(a): ")
aluno2 = input("Digite o nome do 2° aluno(a): ")
aluno3 = input("Digite o nome do 3° aluno(a): ")
aluno4 = input("Digite o nome do 4° aluno(a): ")
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print("O aluno sorteado foi {}.".format(sorteio))
