import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos en un dataframe de Pandas
df = pd.read_csv('datos.csv')

# Crear un histograma de los valores de la columna 'columna_existente'
plt.hist(df['columna_existente'])

# Configurar el título y etiquetas de los ejes
plt.title('Histograma de la columna existente')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()
