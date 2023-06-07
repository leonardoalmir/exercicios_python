cinza = '\033[;37m'
azulClaro = '\033[;36m'
limpa = '\033[m'
print("""{}
==================== DESAFIO 027 ======================
Faça um programa que leia o nome cmpleto de uma pessoa,
mostrando em seguinda o primeiro e o último nome
separadamente. Ex:
Ana Maria Amaral
> Primeiro nome: Ana
> Último nome: Amaral
=======================================================\n{}""".format(cinza, limpa))
nome = input("Digite o nome completo: ").strip()
separado = nome.split()
primeiro = separado[0]
ultimo = separado[len(separado)-1]
print("Primeiro nome: {}{}{}.".format(azulClaro, primeiro, limpa))
print("Último nome: {}{}{}.".format(azulClaro, ultimo, limpa))