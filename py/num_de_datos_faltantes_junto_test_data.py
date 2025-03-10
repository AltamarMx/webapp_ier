# %%
import pandas as pd
import numpy as np
from glob import glob
# %%
def importar_datos(path: str) -> pd.DataFrame:
    data_frame = pd.read_csv(
    path,
    skiprows=[0,2,3],
    index_col=0,
    parse_dates=True,
    dayfirst=True,
    )
    del data_frame["RECORD"]
    return data_frame

def proporcion_faltantes(data_frame: pd.DataFrame) -> float:
    # Eliminar la primera fila si está completamente vacía
    if data_frame.iloc[0].isna().all():
        data_frame = data_frame.iloc[1:]

    # Asegurarse de que el índice es de tipo datetime
    data_frame.index = pd.to_datetime(data_frame.index)

    # Eliminar duplicados en el índice
    data_frame = data_frame.loc[~data_frame.index.duplicated(keep='first')]

    # Obtener el año del primer dato (asumiendo que todos los datos son del mismo año)
    year = data_frame.index.year[0]

    # Crear el rango de fechas completo para ese año
    start_date = f'{year}-01-01 00:00:00'
    end_date = f'{year}-12-31 23:00:00'
    full_index = pd.date_range(start=start_date, end=end_date, freq='H')

    # Reindexar para llenar los huecos con NaN
    data_frame = data_frame.reindex(full_index)
    #Funcion para encontrar la proporcion de daltos faltantes
    total_filas = len(data_frame)
    faltantes = data_frame.isna().sum()  # Por columna
    proporcion_faltantes = faltantes / total_filas

    #Aca se determina si es recomendable imputar los datos

    porcentaje = round(proporcion_faltantes.max()*100,2)
    if porcentaje < 5:
        recomendacion = "Es seguro imputar"
    elif porcentaje < 20:
        recomendacion = "Utiliza met avanzados"
    elif porcentaje < 40:
        recomendacion = "Revisar si las faltas son aleatorias"
    else:
        recomendacion = "Mejor no imputar"
    print(f'Tenemos {porcentaje}% de datos faltantes, podemos recomendar {recomendacion}')
    return porcentaje, recomendacion
    #return print(proporcion_faltantes)

# %%
paths = glob("../data/001_raw/RUOA/Datos_hora/*")
#Se eliminan las rutas de los ultimos 3 archivos ya que tienen un 
#error con el encoding y eso es otro ejercicio
paths = paths[:-4]
paths

# %%
proporcion_faltantes(importar_datos(paths[0]))
