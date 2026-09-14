# %%

import pandas as pd

dados = {
    "idCliente": [101, 102, 103, 104, 105, 106],
    "nome": ["Ana", "Bruno", "Carlos", "Julia", "Pedro", "Marina"],
    "idade": [25, 32, 28, 35, 22, 30],
    "qtdePontos": [500, 1200, 300, 900, 1200, 700]
}

df = pd.DataFrame(dados)

df
# %%

df["qtdePontos"].sort_values(ascending=False) 
# %%
max_pontos = df["qtdePontos"].max() #crio uma variavel com um valor max (vindo de uma função em pandas)

filtro = df["qtdePontos"] == max_pontos #crio um filtro 

df[filtro] #aplico esse filtro no dataframe

# %%

df.sort_values(by="qtdePontos", ascending=False).head(5)
# %%

top_5 = df.sort_values( by= "qtdePontos", ascending=False).head(5)

top_5
# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["Teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533],
    }
)

brinquedo
# %%

salarios_ordenados = brinquedo.sort_values(by= "salario", ascending= False).head(1)


salarios_ordenados
# %%


salarios_ordenados_idade = brinquedo.sort_values(by= ["salario", "idade"], ascending=[False, True])

salarios_ordenados_idade