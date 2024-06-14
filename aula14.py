# Instalando a biblioteca da panda
    # python -m pip install matplotlib
import matplotlib.pyplot as plt

# Construindo um gráfico na mão

# Vetores para minhas medições de X e Y
x = [1,2,3,4,5,6]
y = [10,20,30,40,50,60]

plt.plot(x, y, label='Dados', color='r', linestyle='--', lw=10.0)

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title(' Título do gráfico')

plt.xticks([0,1,2,3,4,5,6,7])
plt.yticks([0,20,40,60])

plt.legend('Legenda')

plt.show()