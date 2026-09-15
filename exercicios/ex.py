# %%

import pandas as pd
# %%

#selecione a primeira transação diária de cada cliente

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes
# %%

transacoes = transacoes.sort_values("DtCriacao")

transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])

# %%

first = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])
last = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])   

pd.concat([last,first])

# %%
