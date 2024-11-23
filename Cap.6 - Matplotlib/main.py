import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Gráfico de linhas(plot)

# x = np.array([1,2,3,4])
# y = x * 2 # broadcast
# y2 = x ** 2

# plt.plot(x, y, '*:g',
#          x, y2, 'o-r', linewidth='5', markersize=20)
# plt.show()


# Sub Plots

# x = np.array([1,2,3,4])
# y = x * 2 # broadcast

# plt.subplot(1,2,1) #1 linha, 2 colunas, Parte 1
# plt.plot(x, y, '*:g', linewidth='5', markersize=20)

# y2 = x ** 2

# plt.subplot(1, 2, 2) #1 linha, 2 colunas, Parte 2
# plt.plot(x, y2, 'o-r', linewidth='5', markersize=20)

# plt.show()

#Scatter plot (gráfico de dispersão)

dfPaises = pd.read_csv('paises.csv', delimiter=';')
print(dfPaises.columns)

dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)')
print(dfPaises2)

plt.scatter(dfPaises2['Country'], dfPaises2['Area (sq. mi.)'], s=dfPaises2['GDP ($ per capita)']/10)
plt.show()


