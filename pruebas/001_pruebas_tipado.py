# %% 
def hola_persona(frase: str, name: str = "mundo") -> None:
    print(f"hola {name} " + frase)
     
def hola_sin_tipado(name):
    print(f"hola {name}")
    

# %%

hola_persona(" cruel", name=3)
hola_sin_tipado(3)


# %%
