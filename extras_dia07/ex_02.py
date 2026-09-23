# %%
import pandas as pd
# %%


transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes.head()
# %%

transacoes.groupby(by=["IdCliente"]).count()

# %%

dados = pd.DataFrame({
    "cliente": ["Ana", "Ana", "Bruno", "Ana", "Bruno", "Carlos"],
    "valor": [100, 200, 50, 300, 80, 120]
})
# %%

dados.groupby(by=["cliente"], as_index=False).count()
# %%

dados.groupby(by=["cliente"], as_index=False)["valor"].count()
# %%
