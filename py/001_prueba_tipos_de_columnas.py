# %% 
import pandas as pd 

# %%
f = "../data/001_raw/RUOA/Datos_hora/2016_RUOA_HR.csv"
data = pd.read_csv(
    f,
    skiprows=[0,2,3],
    index_col=0,
    parse_dates=True,
    dayfirst=True,
    # usecols=[]
    )

del data["RECORD"]

# %%


columnas = data.columns
tipos_esperados_columnas = {columna:"float64" for columna in columnas}


def revisar_tipos_columnas(tipos_esperados_columnas, data):
    tipos_obtenidos_columnas = {columna:f'{data[columna].dtype}'  for columna in columnas}


    for key in set(tipos_esperados_columnas.keys()).union(tipos_obtenidos_columnas.keys()):
        esperado = tipos_esperados_columnas.get(key, None)
        obtenido = tipos_obtenidos_columnas.get(key, None)
        
        if esperado != obtenido:
            print(f"En la llave '{key}' se espera: {esperado} pero se obtuvo: {obtenido}")


revisar_tipos_columnas(tipos_esperados_columnas, data)

