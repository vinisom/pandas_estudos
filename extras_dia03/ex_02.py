# %%
import pandas as pd
# %%
import pandas as pd

df = pd.DataFrame({
    "jogador": ["Yuri", "Memphis", "Garro", "Hugo", "Bidon", "Romero", "Matheuzinho"],
    "idade": [28, 32, 27, 26, 20, 33, 25],
    "gols": [12, 8, 6, 1, 3, 10, 2],
    "valor": [15, 12, 10, 5, 8, 4, 7],
    "posicao": ["ATA", "ATA", "MEI", "GOL", "MEI", "ATA", "LAT"]
})

df
# %%

# Crie um filtro que 
# selecione jogadores com idade maior ou igual a 28 
# e depois aplique o filtro no DataFrame.
filtro = df["idade"] >= 28

df[filtro]

# %%

# Crie um filtro que selecione jogadores com mais de 5 gols.

filtro = df["gols"] > 5

df[filtro]

# %%

#Selecione jogadores cujo valor seja menor ou igual a 8.

filtro = df["valor"] <=8

df[filtro]

# %%

# Agora use &: selecione jogadores que tenham idade menor que 30 E mais de 5 gols.

filtro = (df["idade"]< 30) & (df["gols"] >5)

df[filtro]
# %%

# Agora use |: selecione jogadores que sejam da posição "ATA" OU "MEI".

filtro = (df["posicao"] == "ATA") | (df["posicao"] == "MEI")

df[filtro]

# %%

df = pd.DataFrame({
    "jogador": ["Yuri", "Memphis", "Garro", "Hugo", "Bidon", "Romero", "Matheuzinho"],
    "idade": [28, 32, 27, 26, 20, 33, 25],
    "gols": [12, 8, 6, 1, 3, 10, 2],
    "valor": [15, 12, 10, 5, 8, 4, 7],
    "posicao": ["ATA", "ATA", "MEI", "GOL", "MEI", "ATA", "LAT"],
    "contrato": ["2027-12-31", "2026-12-31", None, "2028-12-31", None, "2026-12-31", "2027-12-31"]
})

# %%

# Usando .isin(), filtre somente jogadores das posições "ATA" e "MEI".

filtro = df["posicao"].isin(["ATA", "MEI"])

df[filtro]

# %%

# Usando .isna(), encontre jogadores que não possuem informação de contrato.

filtro = df["contrato"].isna()

df[filtro]

# %%

# Usando .notna(), encontre jogadores que possuem informação de contrato.

filtro = df["contrato"].notna()

df[filtro]
# %%

#Faça novamente o exercício 2, mas desta vez usando ~ junto com .notna().


filtro = ~df["contrato"].notna()

df[filtro]

# %%
# Desafio: jogadores que sejam "ATA" ou "MEI" E tenham mais de 5 gols.

filtro = (df["posicao"].isin(["ATA", "MEI"])) & (df["gols"]> 5)

df[filtro]

# %%

# Selecione jogadores com idade entre 25 e 30 anos, inclusive.

filtro = (df["idade"] >= 25) & (df["idade"] <= 30)

df[filtro]

# %%

# Selecione jogadores que sejam ATA, MEI ou LAT.

filtro = df["posicao"].isin(["ATA", "MEI", "LAT"])

df[filtro]
# %%

# Encontre jogadores com valor menor que 10 e que possuam contrato informado.

filtro = (df["valor"] < 10) & (df["contrato"].notna())

df[filtro]

# %%

# Encontre jogadores que não sejam ATA.

filtro = ~df["posicao"].isin(["ATA"])

df[filtro]

# %%

# Desafio final: selecione jogadores que:

# sejam ATA ou MEI;
# tenham mais de 5 gols;
# e possuam contrato informado.

filtro = (df["posicao"].isin(["ATA", "MEI"])) & (df["gols"] > 5) & (df["contrato"].notna()) 

df[filtro]
# %%
