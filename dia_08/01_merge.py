# %%

import pandas as pd

# %%

transacoes = pd.read_csv("../data/transacoes.csv",sep=";")

transacoes.head()

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head()

# %%

transacoes.merge(
        clientes,
        how="left",
        left_on="IdCliente",
        right_on="idCliente",
        suffixes= ["Transacao", "Cliente"] #entender como funciona
)

# "Quero juntar transacoes com clientes. Mantenha todas as transações e procure o cliente correspondente usando IdCliente de transacoes e idCliente de clientes."

# transacoes.merge(right=clientes, how='left', on=["idCliente"]) -> aqui esta certo porém no csv ficou transacoes = IdCLiente / clientes = idCliente
#precisarei de exemplos como esse para estudar
#se apareceu algo: coluna_x são colunas redundantes

#how como definimos a interferência(?)

# %%

df_1 = pd.DataFrame({
    "transacao": [1, 2, 3, 4, 5],
    "idCliente": [1, 2, 3, 2, 2],
    "valor": [10, 45, 32, 17, 87],
})

df_2 = pd.DataFrame({
    "id": [1,2,3,4],
    "nome":["teo", "nah", "mah", "jose"]
})

df_2

df_1.merge(df_2,left_on=["idCliente"], right_on=["id"],
           how='left')

# %%

df_1 = pd.DataFrame({
    "transacao": [1, 2, 3, 4, 5],
    "nome": ["t1", "t2", "t3", "t4", "t5"],
    "idCliente": [1, 2, 3, 2, 2],
    "valor": [10, 45, 32, 17, 87],
})

df_2 = pd.DataFrame({
    "id": [1,2,3,4],
    "nome":["teo", "nah", "mah", "jose"]
})

df_2


df_1.merge(df_2,left_on=["idCliente"], right_on=["id"],
           how='left', suffixes=["Transacao", "Cliente"])

# %%

