# %%

import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", None, "Julia", "Pedro"],
    "idade": [25, None, 30, 28, 35],
    "salario": [3000, 4000, 3500, None, 5000]
}

df = pd.DataFrame(dados)

df
# %%

df.dropna() 

#o Pandas vai remover do resultado qualquer linha
#que tenha pelo menos um valor ausente.

# %%

df.dropna(how="all")
 #remova a linha somente se TODOS os valores da linha forem ausentes.

# %%

df.dropna(how="any")

#Basta encontrar pelo menos um NaN na linha para ela ser removida.

# %%

df.dropna(how="all", subset=["idade","salario"])
# %%
df.dropna(how="any", subset=["idade","salario"])

subset=["idade", "salario"]

# how="all"
# → idade E salario precisam ser NaN
# → todos

# how="any"
# → idade OU salario precisa ser NaN
# → pelo menos um

# %%

df.fillna({"nome":"desconhecido", "salario": 0})
# %%

medias = df[["idade"]].mean()

df.fillna(medias)

# %%
