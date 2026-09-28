# %%
import pandas as pd

transacoes = pd.DataFrame({
    "idTransacao": [1, 2, 3, 4, 5],
    "idCliente": [101, 102, 103, 102, 104],
    "valor": [100, 250, 80, 150, 300]
})

clientes = pd.DataFrame({
    "idCliente": [101, 102, 103, 105],
    "nome": ["Ana", "Bruno", "Carlos", "Julia"]
})
# %%

transacoes
# %%
clientes
# %%

transacoes.merge(right=clientes, how='outer', on=["idCliente"])

# %%

transacoes = pd.DataFrame({
    "idTransacao": [1, 2, 3, 4],
    "IdCliente": [101, 102, 103, 104],
    "valor": [100, 250, 80, 300]
})

clientes = pd.DataFrame({
    "id": [101, 102, 103, 105],
    "nome": ["Ana", "Bruno", "Carlos", "Julia"]
})
# %%

transacoes.merge(right=clientes, how='left', left_on=["IdCliente"], right_on=["id"])

# %%

df_1 = pd.DataFrame({
    "transacao": [1, 2, 3, 4, 5],
    "nome": ["t1", "t2", "t3", "t4", "t5"],
    "idCliente": [1, 2, 3, 2, 2],
    "valor": [10, 45, 32, 17, 87]
})

df_2 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nome": ["teo", "nah", "mah", "jose"]
})


# %%
df_1
# %%
df_2
# %%

df_1.merge(
    df_2,
    left_on="idCliente",
    right_on="id",
    how="left",
    suffixes=["Transacao", "Cliente"]
)
# %%
