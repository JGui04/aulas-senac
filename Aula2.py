""" 
Programa: Média de aluno
Autor: J. Guilherme
licença: GNU
Data: 2024/04/26
Versãõ: v1
Descrição: Este programa terá como proposta calcular a média do aluno e sua matéria
"""



# Criar as variáveis para entrada de dados 


"""
nome = "José Guilherme"
materia = "Programação"
n1 = float(5.8)
n2 = float(8)
n3 = float(6.5) 
"""

nome = str(input("Digite o nome do aluno(a):\n"))
materia = str(input("Digite a sua matéria:\n"))
n1 = float(input("Digite a nota da 1ª avaliação:\n"))
n2 = float(input("Digite a nota da 2ª avaliação:\n"))
n3 = float(input("Digite a nota da 3ª avaliação:\n"))

# Processar o valor da media baseado nas notas

media = (n1+n2+n3)/3

#resp = "média"

# Estruturas condicional SE simples
if media >= 5:
    resp = "média satisfatória"

# Estrutura de condicional SE composta
if (media >= 5):
    resp = "média satisfatória"
else:
    resp = "média insatisfeita"

# Imprime na tela o nome, a materia e a media calculada

print(f"O(A) Aluno(a), {nome}, na máteria de {materia} obteve a {resp} de {media}.")