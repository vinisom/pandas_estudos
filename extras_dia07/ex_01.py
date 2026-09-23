# %%
import pandas as pd

# %%

idades = [32, 44, 12, 54, 67, 32, 23, 34, 32, 12, 45, 43, 28, 73, 29]
# %%

type(idades)

# %%

idades = pd.Series(idades)

# %%

idades.sum()
# %%
idades.min()

# %%
idades.max()
# %%
idades.mean()
# %%
idades.describe()

# %%
notas = [7,8,5,10,6]

notas = pd.Series(notas)

notas.max()
notas.min()
notas.mean()
notas.sum()


# %%

twitch = [1, 0, 1, 1, 0, 1, 0, 0]

twitch = pd.Series(twitch)

twitch.sum()
twitch.mean()
# %%
twitch.sum()
twitch.mean()