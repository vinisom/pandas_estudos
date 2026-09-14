# %%

import pandas as pd
import numpy as np

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Julia", "Pedro"],
    "qtdePontos": [0, 100, 500, 1000, 10000],
    "flEmail": [1, 1, 0, 1, 1],
    "flTwitch": [0, 1, 1, 1, 1],
    "flYouTube": [1, 1, 0, 1, 1],
    "flBlueSky": [0, 1, 0, 1, 1],
    "flInstagram": [1, 1, 1, 1, 1]
}

df = pd.DataFrame(dados)

df
# %%

df["pontos_50"] = df["qtdePontos"] + 50
df
# %%

df["qtdSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"] 
df

# %%


df["todasSocial"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"] 
df

# %%

df["qtdePontos"].describe()


# %%

import numpy as np
# %%

df["LogPontos"] = np.log(df["qtdePontos"] +1)

df
# %%
df["LogPontos"].describe()
# %%
import matplotlib.pyplot as plt
# %%

plt.hist(df["LogPontos"])
plt.grid(True)
plt.show()
# %%
