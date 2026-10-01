# %%

import pandas as pd
import os #o que que ele faz?

# exercicio que ele usou para fazer
# %%

def read_file(file_name:str):
    df = (pd.read_csv(f"../data/ipea/{file_name}.csv", sep=";")
            .rename(columns={"valor":file_name})
            .set_index(["nome", "período"])
            .drop(["cod"], axis=1))
          
    return df 


# %%

file_name = os.listdir("../data/ipea/")

dfs = []
for i in file_name:
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))

# %%

df_full = (pd.concat(dfs, axis= 1)
            .reset_index()
            .sort_values(["período","nome"]))

df_full.to_csv("homicidios_consolidado.csv", index=False, sep=";")
# %%

