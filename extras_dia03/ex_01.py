# %%

import pandas as pd
# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")

df.head()

# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 1, 1, 30, 25, 50]

filtro = []
# %%
for i in pontos:
    filtro.append(i >= 50)

filtro

# O filtro não guarda inicialmente os números.

# Ele guarda:

# True ou False para cada posição.
# %%

resultado = []

for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado

# %%
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"],
    }
)
# %%
filtro = brinquedo["idade"] >= 18

brinquedo[filtro]
# %%

# 1. Escolho uma coluna
#         ↓
# brinquedo["idade"]

# 2. Faço uma condição
#         ↓
# brinquedo["idade"] >= 18

# 3. Pandas produz True/False
#         ↓
# True
# True
# False

# 4. Uso isso para filtrar o DataFrame
#         ↓
# brinquedo[filtro]

# 5. Só permanecem as linhas True

# %%


filtro = df["QtdePontos"] >= 50

df[filtro]

# %%

filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)

df[filtro]

# %%

filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)

df[filtro]

# %%

filtro = ( df["QtdePontos"] >0 ) & (df["QtdePontos"] <= 50) | (df["DtCriacao"] >= '2025-01-01')

df[filtro]

# %%

#         COLUNA
#            ↓
# df["QtdePontos"]

#            ↓
#        CONDIÇÃO
# df["QtdePontos"] >= 50

#            ↓
#    SERIES DE BOOLEANOS
# True
# False
# True
# False
# ...

#            ↓
#     APLICA O FILTRO
# df[filtro]

#            ↓
# SÓ AS LINHAS COM TRUE

# | Pandas | Significado    | SQL         |
# | ------ | -------------- | ----------- |
# | `==`   | igual          | `=`         |
# | `!=`   | diferente      | `<>` / `!=` |
# | `>`    | maior          | `>`         |
# | `<`    | menor          | `<`         |
# | `>=`   | maior ou igual | `>=`        |
# | `<=`   | menor ou igual | `<=`        |
# | `&`    | **E**          | `AND`       |
# | `\|`   | **OU**         | `OR`        |
