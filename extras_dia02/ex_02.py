# %%
import pandas as pd

# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")
# %%
df.shape
# %%
df.info(memory_usage="deep")
# %%
df.dtypes
# %%
renamed_columns = {
    "QtdePontos": "QtPontos",
    "DescSistemaOrigem": "SistemaOrigem"
}

df.rename(columns=renamed_columns, inplace=True)

# Então sua frase pode ser:

# inplace=True aplica a alteração diretamente no objeto, então nesse caso não preciso fazer df

# df ["IdCliente", "QtPontos"] maneira errada 

# df[ ["IdCliente", "QtPontos"] ]
#    ↑                          ↑
#    └──────── lista ───────────┘

# df["coluna"]
#        ↓
#      Series


# df[["coluna"]]
#        ↓
#     DataFrame


# df[["coluna1", "coluna2"]]
#        ↓
#     DataFrame

# %%

df[["IdCliente", "QtPontos"]]


# %%

colunas = ["IdCliente", "QtPontos"]

df[colunas]

# %%

df["IdCliente"]

# %%

colunas = df.columns.tolist()
# %%
df.columns.to_list()
# %%

colunas.sort()

df = df[colunas]

df
# %%
