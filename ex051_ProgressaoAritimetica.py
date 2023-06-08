cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 051 ======================
Desenvolva um programa que leia o primeiro termo e a 
razão de uma PA. No final, mostre os 10 primeiros 
termos dessa progressão.
=======================================================\n{}""".format(cinza, limpa))
print("=-"*15)
print("    ", "10 TERMOS DE UMA PA")
print("=-"*15)
n1 = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
an = n1 + (10-1)*razao
for cont in range (n1, an+1, razao):
    print(cont, end=" -> ")
print("Acabou.")
