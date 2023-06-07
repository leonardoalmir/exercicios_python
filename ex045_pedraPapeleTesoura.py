import random
import time

vermelho = '\033[;31m'
verde = '\033[;32m'
cinza = '\033[;37m'
amarelo = '\033[;33m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 045 ======================
Crie um programa que faça o computador jogar Jokenpô
(pedra, papel e tesoura) com você.
=======================================================\n{}""".format(cinza, limpa))
lista = ["Pedra", "Papel", "Tesoura"]
escolha_comp = random.choice(lista)
#print(escolha_comp)
print("=-"*10, " Vamos Jogar! ","=-"*10)
print(azulClaro + "Deixe-me pensar aqui... haha!" + limpa)
time.sleep(2)
print(azulClaro + "Eu estou pronto! Agora é você:" + limpa)
print('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
escolha = int(input("Qual é sua jogada? "))
if escolha == 1:
    escolha_jogador = "Pedra"
elif escolha == 2:
    escolha_jogador = "Papel"
elif escolha == 3:
    escolha_jogador = "Tesoura"

if escolha < 1 or escolha > 3:
    print("Essa opção não existe. Tente novamente!")
else:
    time.sleep(1)
    print("JO...")
    time.sleep(1)
    print("KEN...")
    time.sleep(1)
    print("PÔ!")
    print("=" * 28)
    print("O computador jogou: {}{}{}.".format(azulClaro, escolha_comp, limpa))
    print("Você jogou: {}{}{}.".format(azulClaro, escolha_jogador, limpa))
    print("=" * 28)
    if escolha_comp == "Papel" and escolha_jogador == "Pedra":
        print("O computador foi o vencedor.")
    elif escolha_comp == "Pedra" and escolha_jogador == "Papel":
        print("Você venceu!!!")
    elif escolha_comp == "Tesoura" and escolha_jogador == "Papel":
        print("O computador foi o vencedor.")
    elif escolha_comp == "Papel" and escolha_jogador == "Tesoura":
        print("Você venceu!!!")
    elif escolha_comp == "Pedra" and escolha_jogador == "Tesoura":
        print("O computador foi o vencedor.")
    elif escolha_comp == "Tesoura" and escolha_jogador == "Pedra":
        print("Você venceu!!!")
    else:
        print("Empatou! Jogue novamente!")
