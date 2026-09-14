# %%

import pandas as pd

# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()
# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 1, 1, 30, 25, 50]
filtro = []


valores_50_mais = []

for i in pontos:
    filtro.append(i >=50)

resultado = []
for i in range(len(pontos)):
    if filtro [i]:
        resultado.append(pontos[i])

resultado

# %%

valores_50_mais = [i for i in pontos if i >= 50]

valores_50_mais

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"],
    }
)

filtro = brinquedo["idade"] >= 18

brinquedo[filtro]
# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# Valores maiores que 50
filtro = df["QtdePontos"]>= 50
df[filtro]
# %%

#Pedir para IA falar sobre tabela verdade e exercicios (Que contemplem filtro de pandas)

#Valores entre 50 (inclusive) e 100

filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
filtro 

# TRUE AND TRUE = TRUE
# #TRUE AND FALSE = FALSE
# FALSE AND TRUE = False
# FALSE AND FALSE = FALSE

# TRUE  + TRUE = TRUE
# #TRUE + FALSE = TRUE
# FALSE + TRUE = TRUE
# FALSE + FALSE = FALSE

# %%

filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)

df[filtro]

# %%

# pontos entre 0 e 50 ou do ano de 2025 para frente
filtro = filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) | (df["DtCriacao"] >= '2025-01-01')
df[filtro]

