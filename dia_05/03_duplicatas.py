# %%
import pandas as pd

# %%

df = pd.DataFrame({
    "nome": ["teo", "lara", "nah", "bia", "mah", "lara", "mah", "mah"],
    "sobrenome": ["calvo", "calvo", "ataide", "ataide", "silva", "silva", "silva", "silva"],
    "salarios": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134]
})

df
# %%
df.drop_duplicates()  #mantem um e apaga

# %%

#como escolher quem vai ser excluido

df.drop_duplicates(keep='last')

# %%
df.drop_duplicates(subset=["nome", "sobrenome"])

# %%

df.drop_duplicates(keep= 'last', subset=["nome", "sobrenome"])

# %%

df = df.sort_values("salarios", ascending=False)

df.drop_duplicates(keep= 'last', subset=["nome", "sobrenome"])
# %%

