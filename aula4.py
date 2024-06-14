# criando um vetor e já com valores atribuidos
frutas = [
    "banana",
    "melão",
    "caqui",
    "uva",
    "maçã",
    "tomate"
]
print(f"posicão 3 é: {frutas[3]}")

compra = frutas [2]
print(f"vou comprar a fruta {compra}\n")
print(f"o valor era {frutas[5]}")
venda = "perâ"

frutas [5] = venda 
print(f"o valor mudo para {frutas[5]}")

#frutas[7] = "Melância" -- não é assim 
frutas.append("melância")

print(f"a fruta adicionada é {frutas [6]}")

# removendo uma posição do vetor 
frutas.remove("melão")
print(f"nova posição 1 é {frutas[1]}")

#quantidade de linhas de index do vetor 
linhas = len(frutas)
print(f"quatidade de indices é {linhas}")