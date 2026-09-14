# %%
import pandas as pd

# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
dfs

# %%
# %%
import requests
from io import StringIO

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

dfs = pd.read_html(StringIO(response.text))

dfs
# %%
type(dfs)
# %%

df_uf = dfs[1]

df_uf.to_csv("ufs.csv", sep=":", index=False)