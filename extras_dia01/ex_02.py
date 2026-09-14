# %%
import pandas as pd

pd.Series()
# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]
# %%

series_idades = pd.Series(idades)

series_idades

# %%
media_idades = series_idades.mean()
media_idades
# %%
summary = series_idades.describe()

print(summary)

# count → quantidade de valores

# mean → média

# std → desvio padrão

# min → menor idade

# 25% → primeiro quartil

# 50% → mediana

# 75% → terceiro quartil

# max → maior idade

# %%

# "Tudo em Python é objeto"

# ATRIBUTO
# ↓
# característica/informação do objeto

# series_idades.dtype


# MÉTODO
# ↓
# ação que o objeto executa

# series_idades.mean()
# series_idades.var()
# series_idades.describe()