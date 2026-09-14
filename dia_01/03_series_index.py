# %%

# ESSA É AULA MAIS IMPORTANTE DE PANDAS
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

series_idades = pd.Series(idades) 

series_idades
# %%
idades [-1]
series_idades[0]

# %%
#Os indicies da serie funcionam da mesma maneira que as chaves dos dicionarios

series_idades = series_idades.sort_values()

series_idades



# %%
series_idades[0]

#indice fica vinculado aquela linha da série. Explique melhor sobre
# %%
series_idades.iloc[0] #AQui falamos de posição
# %%
series_idades.iloc[-1]

series_idades.iloc[::-1]
# %%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

series_idades = pd.Series(idades, index=indexs)

# %%
series_idades


# %%
series_idades.iloc[-1]

#Iloc navegar nas linhas
#Loc navegar nos indices