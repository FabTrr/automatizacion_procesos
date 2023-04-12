# Automatización de Procesos con Python 🐍

Muchas veces ocurre que, si recién comenzamos en este mundo, no tenemos gran idea exactamente de qué se trata esto de "automatizar"

Por eso me interesa dejar un ejemplo básico de automatización con Python para manipulación y análisis de datos, limpieza y transformación, generación de informes automatizados, integración de diferentes fuentes de datos, entre otros.. Por supuesto, la base de datos y sus tablas son ficticias para el ejemplo, pero adaptable a cualquier caso básico real.

```python

import pandas as pd
import numpy as np
import sqlalchemy as db

# Conexión a la base de datos SQL
engine = db.create_engine('postgresql://user:password@host:port/database')
connection = engine.connect()

# Consulta a la base de datos para obtener datos
query = "SELECT * FROM tabla_datos WHERE fecha >= '2022-01-01'"
data = pd.read_sql(query, connection)

# Limpieza y transformación de datos
data['columna_nueva'] = data['columna_existente'].apply(lambda x: x**2)
data = data.dropna()

# Generación de informes automatizados
informe = data.groupby('categoria').agg({'columna_nueva': ['mean', 'std']})
informe.to_csv('informe.csv')

# Integración de diferentes fuentes de datos
otra_fuente = pd.read_csv('datos_externos.csv')
data_final = pd.merge(data, otra_fuente, on='id_cliente')

# Cierre de la conexión a la base de datos
connection.close()

```

Este ejemplo particular y sencillo realiza lo siguiente:

* Conecta a una base de datos SQL y consulta los datos.
* Realiza limpieza y transformación de datos.
* Genera un informe automatizado.
* Integra datos de otra fuente externa.
* Cierra la conexión a la base de datos.

Este es solo un ejemplo ilustrativo y simplificado, pero da una idea de cómo se podría automatizar un proceso de manipulación y análisis de datos en Python.

# Codigo explicado paso a paso

```python
import pandas as pd
import numpy as np
import sqlalchemy as db

# Conexión a la base de datos SQL
engine = db.create_engine('postgresql://user:password@host:port/database')
connection = engine.connect()
```

Aquí se importan las bibliotecas de Pandas, NumPy y SQLAlchemy. Después, se establece una conexión a la base de datos a través de SQLAlchemy pasándole el tipo de base de datos, la dirección del servidor, el nombre de usuario y la contraseña.

```python
# Consulta a la base de datos para obtener datos
query = "SELECT * FROM tabla_datos WHERE fecha >= '2022-01-01'"
data = pd.read_sql(query, connection)
```
Aquí se hace una consulta a la base de datos SQL. Se seleccionan todas las columnas de la tabla 'tabla_datos' donde la fecha es igual o posterior a 2022-01-01. Los resultados de la consulta se almacenan en un objeto de Pandas DataFrame llamado data.

```python
# Limpieza y transformación de datos
data['columna_nueva'] = data['columna_existente'].apply(lambda x: x**2)
data = data.dropna()
```
Aquí se limpian y se transforman los datos en el DataFrame data. Se agrega una nueva columna llamada columna_nueva que se calcula elevando al cuadrado los valores de la columna existente columna_existente. También se eliminan todas las filas que tienen valores faltantes.

```python
# Generación de informes automatizados
informe = data.groupby('categoria').agg({'columna_nueva': ['mean', 'std']})
informe.to_csv('informe.csv')
```
Aquí se realiza una agregación de datos por categoría y se genera un informe en formato CSV. Se agrupan los datos por la columna categoria y se calculan la media y la desviación estándar de la columna columna_nueva. El resultado se almacena en un nuevo DataFrame llamado informe, y luego se exporta el informe a un archivo CSV.

```python
# Integración de diferentes fuentes de datos
otra_fuente = pd.read_csv('datos_externos.csv')
data_final = pd.merge(data, otra_fuente, on='id_cliente')
```

Aquí se integran datos de otra fuente externa mediante la biblioteca Pandas. Se lee un archivo CSV llamado datos_externos.csv y se almacena en un nuevo DataFrame llamado otra_fuente. Luego, se fusionan los datos de data y otra_fuente en un solo DataFrame utilizando la columna id_cliente como clave.

```python
# Cierre de la conexión a la base de datos
connection.close()
```

Finalmente, se cierra la conexión a la base de datos.

En resumen, este código realiza tareas de manipulación y análisis de datos. Primero, se conecta a una base de datos SQL y se consulta los datos. Luego, se realiza una limpieza y transformación de los datos y se genera un informe automatizado. Después, se integran datos de otra fuente externa y se fusionan con los datos originales. Finalmente, se cierra la conexión a la base de datos.

# Adicional: crear un histograma de los valores de una columna utilizando Matplotlib:

```python
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
```

Este código carga los datos de un archivo CSV en un dataframe de Pandas, crea un histograma de los valores de una columna utilizando la función hist() de Matplotlib, y configura el título y etiquetas de los ejes utilizando las funciones title(), xlabel() y ylabel(). Finalmente, muestra el histograma utilizando la función show().
