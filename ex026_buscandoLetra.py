print("""
=================== DESAFIO 026 =====================
Faça um programa que leia uma frase pelo teclado e  
smostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
=====================================================\n""")

frase = input("Digite uma frase: ").strip()
maiusucula = frase.upper()
countA = maiusucula.count("A")
print("A letra 'A' aperece {} vezes.".format(countA))
print("A primeira letra 'A' apereceu na posição {}.".format(maiusucula.find("A")+1))
print("A última letra 'A' apareceu na posição {}.".format(maiusucula.rfind("A")+1))
print(maiusucula)