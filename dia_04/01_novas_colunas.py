# %%

import pandas as pd

clientes = df = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head()


# %%

clientes["Pontos_100"] = clientes["qtdePontos"] + 100

clientes.head()

# %%

clientes["emailTwich"] = clientes["flEmail"] + clientes["flTwitch"]

clientes

# %%

clientes["flEmail"] * clientes["flTwitch"]

# %%

clientes["qteSocial"] = clientes ["flEmail"] +	clientes["flTwitch"]+ clientes["flYouTube"]	+ clientes["flBlueSky"]	+ clientes  ["flInstagram"]

clientes
# %%

clientes["Todas_social"] = clientes ["flEmail"] *	clientes["flTwitch"]* clientes["flYouTube"]	* clientes["flBlueSky"]	* clientes  ["flInstagram"]

clientes

# %%

clientes["qtdePontos"].describe()

# %%

import numpy as np
# %%

clientes["logPontos"] = np.log(clientes["qtdePontos"] +1) #me explicar log pq nao lembro e dar exemplos e pq é usado em pandas
# %%

clientes["logPontos"].describe()

# %%

import matplotlib.pyplot as plt


# %%

plt.hist(clientes["logPontos"])
plt.grid(True)
plt.show()
# %%
