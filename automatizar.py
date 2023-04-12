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
