# %%

import pandas as pd

# %%
df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],

})

df
# %%
df_02 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome":["kozato","laura", "dan"],
    "idade": [32,29,31]
})

df_02

# %%

df_03 = pd.DataFrame({
    "idade": [32,34,19,54,33]
})

df_03
# %%

dfs = [df,df_02]
# %%

pd.concat(dfs)

# %%

pd.concat(dfs, ignore_index=True)

# %%

df_a = pd.DataFrame({
    "produto":["arroz","feijão","carne"],
    "preço": [20,10,40]
})

df_a
# %%

df_b = pd.DataFrame({
    "produto": ["leite","café"],
    "preço": [6,15]
})

df_b
# %%

dfs1 = [df_a, df_b]

pd.concat(dfs1)

# %%

pd.concat(dfs1, ignore_index=True)
# %%

df_03 = df_03.sort_values(by="idade")

df_03 = df_03.sort_values(by="idade").reset_index(drop=True)

# %%
pd.concat([df, df_03], axis=1)

# %%

idades = pd.DataFrame({
    "idade": [40, 18, 35, 22]
})

# %%
idades = idades.sort_values(by="idade").reset_index(drop=True)
idades

# %%
nomes = pd.DataFrame({
    "nome": ["Ana", "João", "Carlos"]
})


#%%
idades = pd.DataFrame({
    "idade": [25, 30, 21]
})

# %%

idades = idades.sort_values(by="idade").reset_index(drop=True)
idades

# %%

human = [nomes, idades]


# %%
pd.concat(human, axis=1)

# %%

times = pd.DataFrame({
    "time": ["Corinthians", "Palmeiras", "Santos"]
})

pontos = pd.DataFrame({
    "pontos": [40, 55, 32]
})
# %%


campeonato = [times, pontos]
campeonato
# %%

pd.concat(campeonato, axis=1)
# %%
df_1 = pd.DataFrame({
    "nome": ["Pedro", "Maria"]
})

df_2 = pd.DataFrame({
    "nome": ["Lucas", "Julia"]
})
# %%

pd.concat([df_1, df_2], ignore_index=True)

# %%

nomes = pd.DataFrame({
    "nome": ["Carlos", "Ana", "Pedro"]
})

# %%
idades = pd.DataFrame({
    "idade": [35, 19, 27]
})
# %%
nomes1 = pd.DataFrame({
    "nome": ["Carlos", "Ana", "Pedro"]
})

idades2 = pd.DataFrame({
    "idade": [35, 19, 27]
})
# %%

pd.concat([nomes1, idades2])

# %%

idades2 = idades2.sort_values(by="idade").reset_index(drop=True)

# %%

pessoas = [nomes1, idades2]

pessoas

# %%

pd.concat(pessoas, axis= 1)