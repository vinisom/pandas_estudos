# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head()
# %%
clientes["Pontos_100"] = clientes["qtdePontos"] + 100

clientes
# %%

clientes["EmailTwich"] = clientes["flEmail"] + clientes["flTwitch"]

clientes

# %%

clientes["qteSocial"] = (
    clientes["flEmail"]
    + clientes["flTwitch"]
    + clientes["flYouTube"]
    + clientes["flBlueSky"]
    + clientes["flInstagram"]
)
# %%

clientes["qtdePontos"].describe()

# %%

import numpy as np

# %%
clientes["logPontos"] = np.log(clientes["qtdePontos"] + 1)


# %%

clientes["logPontos"].describe()

# %%

import matplotlib.pyplot as plt
# %%

plt.hist(clientes["logPontos"])

plt.grid(True)

plt.show()
# %%
