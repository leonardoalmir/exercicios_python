print("""
=================== DESAFIO 025 =====================
Crie um programa que leia o nome de uma pessoa e diga 
se ela tem "Silva" mo nome.
=====================================================\n""")

nome = input("Digite um nome: ").strip()
nomeMaiusc = nome.upper()
print("Esse nome tem Silva? {}".format("SILVA" in nomeMaiusc))
