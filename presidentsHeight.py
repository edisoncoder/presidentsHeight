import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("height2.csv")

height = np.array(data["altura(cm)"])

plt.hist(height)
plt.title("Distriuição das Alturas dos Presidentes dos EUA") #Título do Gráfico
plt.xlabel("Altura(cm)") #Label X - Alturas em cm
plt.ylabel("Qtd") #Label Y - frequência das ocorrências
plt.show() #Exibe o gráfico