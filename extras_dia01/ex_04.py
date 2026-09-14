# %%

import pandas as pd

# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

# POSIÇÃO     NOME       IDADE

#    0         Téo         32
#    1         Maria       38
#    2         Jose        30
#    3         Luis        30
#    4         Ana         31
#    ...
# %%
series_idades = pd.Series(idades)

series_idades

series_nomes = pd.Series(nomes)

series_nomes
# %%
df = pd.DataFrame()
# %%
df["idades"] = series_idades
# %%
df["nomes"] = series_nomes

df

# %%
df.loc[0]

# DATAFRAME

#          idades     nomes
# 0          32        Téo   ← pega essa linha
# 1          38        Maria
# 2          30        Jose

#               ↓

#            SERIES

# idades     32
# nomes      Téo

# %%

df.loc[0]["nomes"]
df.iloc[-1]["idades"]

# %%

df.loc[2]["nomes"]

# %%
df.iloc[1]["idades"]

# %%
df.iloc[-1]["nomes"]
# %%
df
# %%
df.loc[3]["idades"] # vou no indice e busco o valor

df.iloc[0]["nomes"] #vou na posição e busco o valor


# %%
jogadores = ["Yuri", "Memphis", "Garro", "Bidon", "Hugo"]
gols = [15, 8, 12, 4, 0]
idades = [25, 32, 28, 21, 26]

series_jogadores = pd.Series(jogadores)
series_gols = pd.Series(gols)
series_idades = pd.Series(idades)

df = pd.DataFrame()

df["jogador"] = series_jogadores
df["gols"] = series_gols
df["idade"] = series_idades

df

# %%
df.index = [101, 205, 310, 415, 520]

df

# %%

df

# %%

df.loc[310]["gols"] #vou no INDICE e retorno com um valor

df.iloc[3]["jogador"] #vou na POSIÇÃO e retonro com um valor

df.loc[520]["idade"] #vou no INDICE e retorno com um valor

df.iloc[0]["idade"] # VOU NA POSIÇÃO e retonro com um valor

#INDICE É O QUE APARECE NA LINHA DA TABELA / POSIÇÃO É O QUE NÃO APARECE

df.loc[415]["jogador"]  #eu vou no INDICE/ DEPOIS VOU PROCURAR O VALOR

df.iloc[0]["idade"] #eu vou na POSIÇÃO/ E DEPOIS RETORNO COM O VALOR QUE EU QUERO

# se eu fizer df.loc[alguma coisa] ele me retorna em forma de serie. mas se eu adicionar outra [alguma coisa] ele retorna alggo específico
# isso vale tambem para o iloc
