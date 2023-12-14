import pandas as pd

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


ruta_csv_proyecto='datasets/annual_deaths_by_causes.csv'

df=pd.read_csv(ruta_csv_proyecto, sep=',')

df['year'] = pd.to_datetime(df['year'] , format='%Y').dt.year

print (df.head())

x=df['year']
y=df['acute_hepatitis']

fig , axs=plt.subplots(figsize=(10, 5))

axs.scatter(x,y, alpha=0.3)
axs.set_title('Evolución de muertes por Hepatitis aguda en el tiempo')
axs.set_xlim([2007, 2019])
axs.set_ylim([3400, 167000])


x3=df['year']
y3=df['nutritional_deficiency']

fig , axs=plt.subplots(figsize=(10, 5))

axs.scatter(x3,y3, alpha=0.3)
axs.set_title('Evolución de muertes por deficiencia en nutricion en el tiempo')
axs.set_xlim([2007, 2019])
axs.set_ylim([3400, 167000])


df_filtered=df[(df['country']=='Argentina')]

nombre_x='year'
nombre_y='acute_hepatitis'
x = df_filtered[nombre_x]
y = df_filtered[nombre_y]

fig, ax=plt.subplots(figsize=(12, 4))

ax.plot(x, y)

ax.set_xlabel(f'{nombre_x}')
ax.set_ylabel(f'{nombre_y}')

ax.set_title(f'{nombre_y} vs {nombre_x} in Argentina')

ax.legend([f'{nombre_y}'])




fig, ax=plt.subplots(figsize=(12, 4))

sns.lineplot(data=df_filtered, x='year', y='hiv/aids')






fig, ax=plt.subplots(figsize=(12, 4))


sns.lineplot(data=df_filtered, x='year', y='acute_hepatitis', label='Hepatitis aguda')

sns.lineplot(data=df_filtered, x='year', y='nutritional_deficiency', label='Nutricion deficiente')

# Añade un título
plt.title('Hepatitis vs Nutricion deficiente a lo largo de los años')

# Muestra la leyenda
plt.legend()

fig, ax=plt.subplots(figsize=(12, 4))

sns.scatterplot(data=df_filtered, x='acute_hepatitis', y='nutritional_deficiency', hue='year')


plt.show()
