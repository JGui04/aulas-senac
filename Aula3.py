# Conhecendo a estrutura condicional CASO
dia = 9
match dia:
    case 1:
        diaSemana = "Domingo"
    case 2:
        diaSemana = "Segunda-Feira"
    case 3:
        diaSemana = "Terça-Feira"
    case 4:
        diaSemana = "Quarta-Feira"
    case 5:
        diaSemana = "Quinta-Feira"
    case 6:
        diaSemana = "Sexta-Feira"
    case 7:
        diaSemana = "Sábado"
    case _:
        diaSemana = "Este dia da semana não existe"

# print(f"\nDia da semana é {diaSemana}.")
if (diaSemana == "Sábado"):
    atividade = "Dormir após a festa"
elif (diaSemana == "Domingo"):
    atividade = "Churrasco"
else:
    atividade = "Trabalhar"
# print(f"\nHoje é: {diaSemana}, logo é dia de {atividade}.\n")

if (diaSemana == "Este dia da semana não existe"):
    print(f"\n{diaSemana}.\n")
elif (diaSemana == "Sábado"):
    atividade = "Dormir após a festa"
    print(f"\nHoje é: {diaSemana}, logo é dia de {atividade}.\n")
elif (diaSemana == "Domingo"):
    atividade = "Churrasco"
    print(f"\nHoje é: {diaSemana}, logo é dia de {atividade}.\n")
else:
    atividade = "Trabalhar"
    print(f"\nHoje é: {diaSemana}, logo é dia de {atividade}.\n")

# estrutura de repetições

lista = [1,2,3,4,5] # vetor de indice simples

for item in lista:
    print(item)
else:
    print("Todos items foram exibidos com sucesso !!")

i = 0

while (i <=10):
    print(f"Valor do contador é {i}")
    i += 1
else:
    print(f"Final do contador é {i}")