# %%

import pandas as pd
# %%

df = pd.read_csv("../data/clientes.csv", sep=";")

df.head()

# %%

df["qtdePontos"].astype(float).astype(str)



# %%

#parecido com o case when

replace = {"0000-00-00 00:00:00.000":"2024-02-01 09:00:00.000"}

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace)) 

# %%

df["DtCriacao"].dt.day
df["DtCriacao"].dt.month
df["DtCriacao"].dt.month_name()
df["DtCriacao"].dt.year
df["DtCriacao"].dt.day_of_week
df["DtCriacao"].dt.date
df["DtCriacao"].dt.daysinmonth

# %%

df["DtCriacao"].dt.month.astype(int)