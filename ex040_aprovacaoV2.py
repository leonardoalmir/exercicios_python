vermelho = '\033[;31m'
verde = '\033[;32m'
cinza = '\033[;37m'
amarelo = '\033[;33m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 040 ======================
Crie um programa que leia duas notas de um aluno e 
calcule sua média, mostrando uma mensagem no final, 
de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
=======================================================\n{}""".format(cinza, limpa))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("A média desse aluno(a) foi {}{}{}.".format(azulClaro,media, limpa))
if media < 5:
    situacao = "\033[;31mReprovado(a)\033[;m."
elif (media >= 5) and (media <= 6.9):
    situacao = amarelo+'Em Recuperação'+limpa+'.'
else:
    situacao = verde+'Aprovado(a)!'+limpa+'.'
print("A situação desse(a) aluno(a) é: {} ".format(situacao))