# Instalando a biblioteca da panda
    # python -m pip install matplotlib
import matplotlib.pyplot as plt

"""
Dados fictícios de exemplo do índice da Bovespa(podendo ser substituido por valores reais)
Lista de valores em um vetor
"""
dadosBovespa = [
    100,102,105,103,101,112,115,113,111,112
]

intervaloTempo = range(0, len(dadosBovespa))

# Plotar o gráfico de linhas
plt.plot(intervaloTempo, dadosBovespa)

plt.xlabel('Tempo(60min)')
plt.ylabel('Valor do índice')

plt.title('Índice Bovespa - Time Frame de - 60min')

plt.show()