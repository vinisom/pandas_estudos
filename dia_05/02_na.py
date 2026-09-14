# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes

# %%

#primeira opção remover todos NaN

# clientes.dropna() #me trás uma view

clientes.dropna() #me trás uma view

# %%
#definidindo regras de dropar NaN

clientes.dropna(how="all") #criteiro: a linha inteira seja NaN

# %%

clientes.dropna(how="any") #encontrar ao menos um nan, apague


# %%

df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453, 4324, None, 5423]
    }
)

df
# %%
df.dropna(how="all")
# %%
df.dropna(how="all", subset=["idade"])
# %%
df.dropna(how="all", subset=["idade","salario"]) # aparece todas
# %%
df.dropna(how="any", subset=["idade","salario"])
# %%
df
# %%
df.dropna(how="all", subset=["idade","nome"])
# %%
df["idade"].fillna(0) #inputando um valor


# %%

df.fillna({"nome":"alguem", "idade": 0})
# %%

medias = df.fillna(df[["idade", "salario"]].mean())
df.fillna(medias)

# %%

df["idade"].fillna(df["idade"]).mean().mean()