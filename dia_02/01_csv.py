# %%
#como importar csv

import pandas as pd

# %%

df = pd.read_csv("../data/clientes.csv", sep=";")

df

# %%

df.to_csv("clientes.csv", index=False)

# %%

df.to_parquet("clientes.parquet", index=False)

# %%
df_2 = pd.read_parquet("clientes.parquet")

df_2
# %%
df.to_excel("clientes.xlsx", index=False)
# %%
df_3 = pd.read_excel("clientes.xlsx")
df_3
# %%
df_bobo = pd.read_csv("../data/bobo.csv",sep=";")

df_bobo
# %%
# %%
import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

print(os.environ["SSL_CERT_FILE"])

# %%

# %%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

dfs = pd.read_html(url)

dfs