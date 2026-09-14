# %%
import pandas as pd
# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]
# %%
series_idades = pd.Series(idades)

idades[0]
# %%

series_idades = series_idades.sort_values()

series_idades.iloc[0] #iloc trabalha com posição

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
# %%

series_idades = pd.Series(idades, index= indexs)
# %%
series_idades.loc["Kozato"]

# %%
idades = [25, 40, 32, 28]

nomes = ["João", "Ana", "Pedro", "Maria"]

serie = pd.Series(idades, index=nomes)
# %%

serie.loc["Pedro"] # AQui eu busco pelo indice e retorna meu valor

serie.iloc[0] #Aqui eu busco pela posição e ele retorna o valor que está naquela posição

serie.iloc[-1] #Aqui eu estou buscando a última posição

# Quero acessar um dado da Series
#             │
#             │
#      Como vou encontrá-lo?
#             │
#        ┌────┴────┐
#        ↓         ↓
#     ÍNDICE     POSIÇÃO
#        ↓         ↓
#      .loc       .iloc

# POSIÇÃO     ÍNDICE     VALOR

#    0         João        25
#    1         Ana         40
# 👉 2         Pedro       32
# %%

import pandas as pd
# %%

jogadores = ["Yuri", "Memphis", "Garro", "Hugo"]
gols = [15, 8, 12, 4, 0]

serie_gols = pd.Series(gols, index=jogadores)
# %%
import pandas as pd

jogadores = ["Yuri", "Memphis", "Garro", "Bidon", "Hugo"]
gols = [15, 8, 12, 4, 0]

serie_gols = pd.Series(gols, index=jogadores)
# # %%
# POSIÇÃO     ÍNDICE       VALOR

#    0         Yuri          15
#    1         Memphis        8
#    2         Garro         12
#    3         Bidon          4
#    4         Hugo           0

serie_gols.loc["Garro"] #Vou no indice e busco o valor que tem nele

serie_gols.iloc[1] # Vou na posição e retorno com o valor dele

serie_gols.iloc[-1] #Vou na última posição e retorno com o valor 

serie_gols.iloc[3] #vou na posição e busco o valor 


serie_gols.loc["Yuri"] #vou no indice e retorno com o valor

# %%
serie_gols = serie_gols.sort_values()

serie_gols

# %%

#sort_values: Ordena os valores

serie_gols.loc["Yuri"] #VOu diretamente ao indice e retorno o valor dela

serie_gols.iloc[0] #VOu na posição e retorno com o valor dela

serie_gols.iloc[4] # VOu na posição e retorno com o calor

