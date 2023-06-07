amarelo = '\033[;33m'
cinza = '\033[;37m'
vermelho = "\033[;31m"
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 037 ======================
Escreva um programa em Python que leia um número 
inteiro qualquer e peça para o usuário escolher qual 
será a base de conversão: 1 para binário, 2 para octal 
e 3 para hexadecimal.
=======================================================\n{}""".format(cinza, limpa))
num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para realizar a conversão: \n"
      "[ 1 ] converter para Binário \n"
      "[ 2 ] converter para Octal \n"
      "[ 3 ] conveter para hexadecimal ")

opcao = int(input("Digite sua opção: "))
if  opcao == 1:
    print("O número {} em Binário é {}.".format(num, format(num, "b")))
elif opcao == 2:
    print("O número {} em Octal é {}.".format(num, format(num, "o")))
elif opcao == 3:
    print("O número {} em Hexadecimal é {}.".format(num, format(num, "x")))
else:
    print("A opção digitada não existe.")