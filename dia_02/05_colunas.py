# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df 
# %%
df.shape

# %%
df.info(memory_usage="deep")

# %%

df.dtypes
# %%
#a chave vai ser o nome antigo da coluna e o valor associado vai ser o nome novo
#ele vai criar um novo dataframe
# por isso vem o df = 
#DEPENDE DA MUDANÇA

renamed_columns = {
     "QtdePontos": "QtPontos", 
     "DescSistemaOrigem": "SistemaOrigem"
                    }

df.rename(columns=renamed_columns, inplace=True)

# %%
df["IdCliente","QtPontos"] #só podemos passar um elemento, segundo o professor

# %%
df[["IdCliente","QtPontos"]] #isso é uma lista que retorna um dataframe

#Se eu mostrar uma lista com um elemento é um dataframe com uma única coluna

#se vc passar df["IdCliente"] uma chave ele retornará uma série
# mas se vc passar df[["IdCliente"] ] uma lista de chaves  ele retornará um dataframe

# isso é importante

# %%
#focar nisso para entender como funcionar 
colunas =["IdCliente", "QtPontos"]

df[colunas]

# %%

#COMPRARAÇÃO COM SQL

# SELECT * FROM df 

df
# %%
 # select idCliente from df

df[["IdCliente"]]

# %%
# select idCLiente from limit 5

df[["IdCliente", "QtPontos"]].sample(5)
df[["IdCliente", "QtPontos"]].tail(5)
# %%

# select idCliente, idTransacao,qtPontos
# from df 
# limit 5

df[["IdCliente", "IdTransacao", "QtPontos"]].head(5)
#Para vc ordenar as colunas do seu dataset é só você reatribuir a ele mesma

# %%

# df[["DtCriacao", "IdCliente","IdTransacao", "QtPontos", "SistemaOrigem"]]

colunas = df.columns.tolist()
colunas.sort()

df = df[colunas]

df