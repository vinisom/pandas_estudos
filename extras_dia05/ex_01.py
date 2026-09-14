# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

df.head()
# %%

pontos = pd.Series([100, 250, 500, 1000])

pontos.astype(int).astype(float).astype(str)

# %%

import pandas as pd

dados = {
    "idCliente": [101, 102, 103, 104, 105],
    "nome": ["Ana", "Bruno", "Carlos", "Julia", "Pedro"],
    "DtCriacao": [
        "2024-01-15 10:30:00.000",
        "0000-00-00 00:00:00.000",
        "2024-03-20 14:45:00.000",
        "2024-04-10 08:15:00.000",
        "0000-00-00 00:00:00.000"
    ]
}

df = pd.DataFrame(dados)

df
# %%

replace = {
    "0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"
}

df["DtCriacao"] = pd.to_datetime(
    df["DtCriacao"].replace(replace)
)


# %%
df["DtCriacao"].dt.daysinmonth


# .astype()        # converte tipos

# .replace()       # substitui valores

# pd.to_datetime() # converte para data/hora

# .dt.day          # dia
# .dt.month        # mês
# .dt.month_name() # nome do mês
# .dt.year         # ano
# .dt.day_of_week  # dia da semana
# .dt.date         # somente a data
# .dt.daysinmonth  # quantidade de dias no mês