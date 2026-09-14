# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")

df_clientes

# %%

#Amostras

df_clientes.head() #parecido com o limit do sql. mostra o inicio
# %%
df_clientes.head(n=10)

# %%
df_clientes.tail(10) #mostra o final do dataset

# %%
df_clientes.sample(10) #vizualizar os sortidos

# %%

df_clientes.shape#ele diz a dimensão, ele não é um método e sim um atributo/ retorna uma tupla com a quantidade de linhas e colunas
# %%
df_clientes
# %%
df_clientes.columns #atributo também que mostra todas as colunas em froma de listas
# %%
df_clientes.index #diz os indices, opandas que cria esse indice pro arquivo? acredito que sim
# %%
df_clientes.info() #passa as informações do dataframe

# %%
df_clientes.info(memory_usage='deep') # fala o valor real da memory usage

# %%
df_clientes.dtypes #mostra uma serie/quero que me explique mais

# %%

df_clientes.dtypes["DtCriacao"]

#dtypes: é uma serie que mostra os valores da tipagem de cada coluna/ vou querer exemplos

# %%

