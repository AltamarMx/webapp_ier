# %% 
import pandas as pd 

# %%
f = "../data/001_raw/RUOA/Datos_hora/2017-RUOA-HR.csv"
pd.read_csv(
    f,
    skiprows=[0,2,3],
    index_col=0,
    parse_dates=True,
    dayfirst=True,
    # usecols=[]
    )


# %%
