import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')
dfSpace = pd.read_csv('space.csv', delimiter=';')

# print (dfSpace.columns)
locationColumn = dfSpace['Location'].unique()
companyEUA = (dfSpace['Location'].str.contains('USA', case=False, na=False)).sum()
companyCHINA = (dfSpace['Location'].str.contains('CHINA', case=False, na=False)).sum()

plt.bar(['company_EUA', 'company_CHINA'], [companyEUA, companyCHINA])
plt.show()


regionColumn = dfPaises['Region']
regionNorthernAmerica = regionColumn.str.contains('NORTHERN AMERICA')
countryNorthernAmerica = dfPaises[regionNorthernAmerica]

plt.plot(countryNorthernAmerica['Country'], countryNorthernAmerica['Birthrate'], 'b-', label='Taxa de Nascimento')
plt.plot(countryNorthernAmerica['Country'], countryNorthernAmerica['Deathrate'], 'r--', label='Taxa de Mortalidade')

plt.xlabel('País')
plt.ylabel('Taxas (%)')
plt.title('Taxas de Nascimento e Mortalidade em Northern America')       
plt.show()

