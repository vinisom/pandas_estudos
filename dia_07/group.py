# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv" ,sep=";")
transacoes.head()

# %%
transacoes.groupby(by=["IdCliente"]).count() #estou contando qunatas linhas de cada envovlendo o idCliente

# %%

transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()

# %%

#quantidade de transacoes, total de pontos e media de pontos por transacoes

summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
            .agg({"IdTransacao": ['count'],
                  "QtdePontos": ['sum', 'mean']})

)

summary
# %%

summary.columns #apareceu mulIndex

# %%

summary(["QtdePontos", "mean"])

# %%

summary.columns = ["idCLiente","qtdeTransacao", "TotalPontos", "avgPontos" ]
summary
# aqui definimos como será nossas colunas

