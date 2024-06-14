# Instalar a biblioteca do panda
# python -m pip install pandas
# python -m pip install openpyxl
import pandas as pd

# Criando vetor como Objeto
vetor = {
    'nome': [
        'Nerildo',
        'Pedro',
        'Alana',
        'José',
        'Alice',
        'Luis'
    ],
    'Idade':[
        43,
        23,
        19,
        20,
        11,
        56
    ]
}


# Criar uma variável para receber os dados do vetor e encapsular dentro de um
# DataFrame
dados = pd.DataFrame(data= vetor)

# Criar o arquivo de Excel
dados.to_excel('NomesAula-11.xlsx', index= False)

print(dados)