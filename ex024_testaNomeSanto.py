print("""
=================== DESAFIO 024 =====================
Crie um programa que leia o nome de uma cidade e diga 
se ela começa com o nome "SANTO".
=====================================================\n""")
cidade = input("Digite o nome de uma cidade: ").strip()
cidadeMinusculo = cidade.lower() #passa a string pra minusculo
print(cidadeMinusculo[:5] == "santo")

""" Jeito um pouco mais complexo.. mas funciona.
cidadeSplit = cidadeMinusculo.split() #Divide a string por palavra sem espaço
print("santo" in cidadeSplit[0]) #Verifica se tem a palavra santo na primeira palavra
"""