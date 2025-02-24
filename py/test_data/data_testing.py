import pandas as pd

def import_data(f, encoding="utf-8"):
    try:
        data = pd.read_csv(
            f,
            skiprows=[0,2,3],
            index_col=0,
            parse_dates=True,
            dayfirst=True,
            encoding=encoding
            # usecols=[]
            )
        del data["RECORD"]
        tag_encoding = True
    except:
        tag_encoding = False
        print(f"Revisa que el encoding sea {encoding} ")

    return data,tag_encoding



def detect_endswith(filepath):
    """Detecta el tipo de archivo basándose en su extensión y contenido."""
    if filepath.endswith('.csv'):
        tag_endswith = True
    else:
        tag_endswith = False
        print("El archivo no termina en csv")
        
    return tag_endswith


def detect_nans(df):
    if df.isnull().sum().sum() == 0:
        tag_nans = True
    else:
        tag_nans = False

    return tag_nans
