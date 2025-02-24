# %%
import pandas as pd
import numpy as np
from glob import glob
# %%
def proporcion_faltantes(f):
    data = pd.read_csv(
    f,
    skiprows=[0,2,3],
    index_col=0,
    parse_dates=True,
    dayfirst=True,
    )
    del data["RECORD"]
    # Eliminar la primera fila si está completamente vacía
    if data.iloc[0].isna().all():
        data = data.iloc[1:]

    # Asegurarse de que el índice es de tipo datetime
    data.index = pd.to_datetime(data.index)

    # Eliminar duplicados en el índice
    data = data.loc[~data.index.duplicated(keep='first')]

    # Obtener el año del primer dato (asumiendo que todos los datos son del mismo año)
    year = data.index.year[0]

    # Crear el rango de fechas completo para ese año
    start_date = f'{year}-01-01 00:00:00'
    end_date = f'{year}-12-31 23:00:00'
    full_index = pd.date_range(start=start_date, end=end_date, freq='H')

    # Reindexar para llenar los huecos con NaN
    data = data.reindex(full_index)
    #Funcion para encontrar la proporcion de daltos faltantes
    total_filas = len(data)
    faltantes = data.isna().sum()  # Por columna
    proporcion_faltantes = faltantes / total_filas
    return proporcion_faltantes
    #return print(proporcion_faltantes)

# %%
paths = glob("../data/001_raw/RUOA/Datos_hora/*")
#Se eliminan las rutas de los ultimos 3 archivos ya que tienen un 
#error con el encoding y eso es otro ejercicio
paths = paths[:-3]
paths

# %%
resultados = []

# Bucle for para aplicar la función a cada archivo y guardar los resultados
for path in paths:
    resultado = proporcion_faltantes(path)  # Llama a la función
    resultados.append(resultado)  # Guarda el resultado en la lista

# %%
print('''Archivo   Porcentaje_faltantes   Recomendacion''')
for i in range(len(paths)):
    archivo = paths[i][-16:-4]
    porcentaje = round(resultados[i].max()*100,2)
    if porcentaje < 5:
        recomendacion = "Es seguro imputar"
    elif porcentaje < 20:
        recomendacion = "Utiliza met avanzados"
    elif porcentaje < 40:
        recomendacion = "Revisar si las faltas son aleatorias"
    else:
        recomendacion = "Mejor no"
    print(f'{archivo}   {porcentaje}   {recomendacion}')

