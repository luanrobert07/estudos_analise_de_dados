import pandas as pd
import matplotlib.pyplot as plt

dfBrands = pd.read_csv('brands.csv', delimiter=';')

#Exercicio 1

columnBrands = dfBrands['Brand']
filterBrandGoogle = columnBrands.str.contains('Google')
brandGoogle = dfBrands[filterBrandGoogle][['Brand', 'Brand Value ($M) in 2021', 'Brand Value ($M) in 2022']]


# brandGoogle['Valuation Increase ($M)'] = brandGoogle['Brand Value ($M) in 2022'] - brandGoogle['Brand Value ($M) in 2021']
valuation_increase = brandGoogle['Brand Value ($M) in 2022'].iloc[0] - brandGoogle['Brand Value ($M) in 2021'].iloc[0]
print(valuation_increase)

#Exercicio 2

columnBrands = dfBrands['Brand']
marcasPalavraGroup = columnBrands.str.contains('Group')
brandPalavraGroup = dfBrands[marcasPalavraGroup]['Brand']
print(len(brandPalavraGroup))

#Exercicio 3

columnBrand = dfBrands['Brand']
fiveBrand = dfBrands.loc[1:5, ['Brand','Brand Value ($M) in 2022']]
aumento10percent = fiveBrand['Brand Value ($M) in 2022'] * 1.10

print(aumento10percent)

#Exercicio 4

slicingColumns = dfBrands.loc[:,['Brand','Founded By/How it was founded', 'Founded In']]
print(slicingColumns[slicingColumns['Founded In'] > 2000])

filteredData = slicingColumns[slicingColumns['Founded In'] > 2000]

plt.plot(filteredData['Brand'], filteredData['Founded In'], color='skyblue')
plt.show()

#Exercicio 5

empresaFundadaColumns = dfBrands['Founded In']
frequenciaDeAnos = empresaFundadaColumns.value_counts()

ano_mais_empresas = frequenciaDeAnos.idxmax()
quantidade_mais_empresas = frequenciaDeAnos.max()

print(f"Ano com mais empresas fundadas: {ano_mais_empresas} ({quantidade_mais_empresas} empresas)")

plt.bar(frequenciaDeAnos.index, frequenciaDeAnos.values)
plt.show()