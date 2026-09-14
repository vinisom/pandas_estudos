# %%

import pandas as pd

# %%

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")

df_clientes

# %%

df_clientes.head() # Aqui ele mostra as primeiras linhas

# %%
df_clientes.head(n=10) # mostra os 10 primeiros

# %%

df_clientes.tail(10) #Olha o Final
# %%

df_clientes.sample(10) #amostra aleatória de 10 linhas
# %%
df_clientes.shape #informa a dimensão do DataFrame

# %%
df_clientes.columns
# %%
df_clientes.columns.tolist()

# %%
df_clientes.index
# %%
df_clientes.info()

# Esse método é como um raio-X do DataFrame.

# Ele apresenta informações como:

# quantidade de linhas
# quantidade de colunas
# nome das colunas
# quantidade de valores não nulos
# tipo de cada coluna
# uso de memória


# %%

df_clientes.info(memory_usage="deep")

# %%
df_clientes.dtypes

# int64    → números inteiros
# float64  → números decimais
# object   → frequentemente texto
# bool     → True/False
# datetime → datas/horários


# %%
df_clientes.dtypes["DtCriacao"]