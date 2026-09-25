# %%

import pandas as pd
# %%

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%

transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")

transacao_produto.head()

# %%

produtos = pd.read_csv("../data/produtos.csv", sep=";")
produtos
# %%

cliente_transacao_produto = transacoes.merge(
                            transaco_produto,
                            on="IdTransacao",
                            how="left",
                            )


cliente_transacao_produto[["IdTransacao","IdCliente", "IdProduto"]]

# %%

df_full = cliente_transacao_produto.merge(
    produtos,
    on=["IdProduto"],
    how="left",
)

df_full.groupby(by=["IdCliente"])["IdTransacao"].count()

# %%

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
 .count()
 .sort_values(ascending=False)
 .head(1)
)

# %%
#Uma maneira um avançada

produtos = produtos[produtos["DescNomeProduto"]=="Presença Streak"]

(transacoes.merge(transacao_produto, on="IdTransacao",how="left")
            .merge(produtos, on=["IdProduto"], how="inner")
            .groupby(by="IdCliente")["IdTransacao"]
            .count()
            .sort_values(ascending=False)
            .head(1)
            )

#Estamos empilhando os comandos sem precisar reatribuir.
#FIltra logo de cara o que vc precisa

