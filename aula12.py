# Instalar a biblioteca do panda
    # python -m pip install pandas
    # python -m pip install openpyxl
    # python -m pip install matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Criar uma variável para receber a planilha do excel
x = pd.read_excel('C:/Users/jose.gflima1/OneDrive - SENAC - SP/Python/Dados Aula 12.xlsx')

# Criando gráfico
# Adicionando o titulo do gráfico
plt.suptitle("Vendas Região - Mensal", fontsize = 16, weight = 'bold')

# plt.plot(x['Valor Final'])

# Gráfico pizza
# plt.pie(x['Valor Final'], labels=x['Região'], autopct='%1.2f%%')

# Gráfico Histograma
plt.hist(x['Valor Final'], bins=20)

# Imprimir o gráfico
plt.show()