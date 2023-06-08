cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 049 ======================
FRefaça o DESAFIO 9, mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um 
laço for.
=======================================================\n{}""".format(cinza, limpa))
numero = int(input("Digite um número: "))
for cont in range (1, 11):
    print("{} x {} = {}".format(numero, cont, numero*cont))