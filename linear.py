import matplotlib.pyplot as plt
import numpy as np

# Valores de a,b,c são os 3 primeiros números do RU
a = 3
b = 8
c = 8

# Criação do vetor aleatório de tamanho 10
x = np.random.rand(10)

# Equação linear
y = a * x + b * x - c

# Criação das cores dos pontos
cores = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'cyan', 'magenta', 'gray', 'black']

#Criação do gráfico da equação linear
for i in range(len(x)):
    plt.scatter(x[i], y[i], color=cores[i], label='({:.2f}, {:.2f})'.format(x[i], y[i]), s=150)
plt.plot(x, y)
plt.xlabel('EIXO X')
plt.ylabel('EIXO Y')
plt.title('Gráfico da Equação Linear (y = ax + bx – c)')
plt.legend()
plt.grid()
