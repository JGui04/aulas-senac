# Primeiro vamos criar um vetor
produto = [
    "a fruta",
    "a quantidade",
    "o preço"
]

# Criando a matriz
matriz = []

matriz.append(produto)

# Criar um loop para permitir que o usuário insira as linhas de matriz
while True:
    linha = []

    # solicite que o usuário insira os valores para cada campo
    for campo in produto:
        valor = input("Digite {}:\n".format(campo))
        linha.append(valor)

    # Adicionada a linha á matriz
    matriz.append(linha)

    resp = int(input("Deseja adicionar outro produto?\n1 - sim\n2 - não\n"))

    if resp != 1:
        break
# Imprimindo a matriz
print("Matriz: ")
for linha in matriz:
    print(" | ". join(linha))