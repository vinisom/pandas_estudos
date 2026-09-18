# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

df.head()
# %%
idCliente = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"


idCliente.split("-")
idCliente.split("-")[-1]

# %%

def get_last_id(x):
    return x.split("-")[-1]

# %%

get_last_id("0019bb9e-26d4-4ebf-8727-fc911ea28a92")
# %%

id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

id_novo


df["novo_id"] = id_novo

df.head()

# %%

df["idCliente"].apply(get_last_id) 
#.apply é uma maneira de vc aplicar métodos, 
#transformações linha a linha, elemento elemento

