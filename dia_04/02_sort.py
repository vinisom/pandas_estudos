# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head()

# %%

#Como eu faço par aordenar

clientes["qtdePontos"].sort_values()
# %%
max_ponto = clientes["qtdePontos"].max()

filtro = clientes["qtdePontos"]== max_ponto

clientes[filtro]
# %%

clientes.sort_values(by="qtdePontos", ascending=False).head(5)
#sort_values retorna um dataframe novo, mas não é uma view

#ele descobre o id do cliente aqui? acho que sim. pedir.

# %%

top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
         .head(5)["idCliente"])

top_5
# %%
type(top_5)

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["Teo","ana", "nah", "jose"],
        "idade":[32, 43, 35, 42],
        "salario":[2345, 4533, 3245, 4533],
    }
)

brinquedo
# %%
brinquedo.sort_values(by="salario", ascending=False)

# %%


brinquedo.sort_values(by=["salario", "idade"], ascending=False)
# %%

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])

#reforçar o sort

