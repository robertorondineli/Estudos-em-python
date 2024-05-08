# Visualizar dados de vendas de produtos em um gráfico de barras
import matplotlib.pyplot as plt

# Dados
x = ["A","B","C","D"]
y = [3,8,1,10]

# Criando gráfico
plt.bar(x, y)

# Título para os eixos
plt.title("Gráfico para Faculdade")
plt.xlabel("X")
plt.ylabel("Y")

# Exibir o gráfico
plt.show()