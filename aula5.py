# Criando matriz bi-dimencional

feira = [
    ["maçã",5,10,50],
    ["banana",12,0.60,7.20],
    ["perâ",6,1,6.00],
    ["melância",3,2,6.00]
]

print(f"o valor da minha coluna 1 e coluna 1 é: {feira[1][1]}")

feira [2][0] = "uva"
print(f"o valor da fruta perâ mudou para: {feira[2][0]}")

compra = feira[3][3]
print(f"Valor da compra da {feira[3][0]} é de R$ {compra}")

# Construindo matriz com uso de funções

def main():
    A = ler_matriz()

    if simetrica(A):
        print("matriz simétrica")
    else:
        print("matriz não é simétrica")

def ler_matriz():
    nL = int(input("Digite o número de linhas de matriz:"))
    nC = int(input("Digite o número de colunas de matriz:"))

    matriz = []
    for i in range(nL):
        linha = []
        for j in range(nC):
            valorC = input("Digite o valor o elemento em (%d,%d): "%(i,j))
            linha.append(valorC)
        matriz.append(linha)
    return matriz

def simetrica(matriz):
    nL = len(matriz)
    nC = len(matriz[0])

    if nL != nC:
        return False
    for i in range(nL):
        for j in range(i):
            if(matriz[i][j] != matriz[i][j]):
                return False
    return True

main()


