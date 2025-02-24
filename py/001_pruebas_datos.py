# %% 
import pandas as pd 
import missingno as msno

from test_data.data_testing import import_data
from test_data.data_testing import detect_endswith
from test_data.data_testing import detect_nans


# %% Prueba de si es CSV]

f ="../data/001_raw/ESOLMET/2015_ESOLMET.csv" 

tag_endswith = detect_endswith(f)

# %% Prueba si es UTF-8
data, tag_encoding = import_data(f)


# %% Detecta si hay nans 

tag_nans = detect_nans(data)

# %%  Construye diccionario de pruebas

tests = {
    "CSV extension":tag_endswith,
    "Encoding UTF-8":tag_encoding,
    "Nans":tag_nans,
    # "Nans":
}

tests
# %%





