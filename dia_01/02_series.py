# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

media = sum (idades) / len(idades)

media
# %%
diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades)-1)

variancia # o que seria variancia e diffs em python? ele usou isso como exemploe e abaixo vai usar o pd.series

# %%

import pandas as pd

series_idades = pd.Series(idades) 

series_idades

#o ideal é ter séries do mesmo tipo
# ele diz que tudo em python é objeto,preciso reforçar métodos e atributos
# %%

# Estatísticas da séries 
media_idades = series_idades.mean()
media_idades


var_idades = series_idades.var()
var_idades
summary = series_idades.describe()
summary

#o do professor deu sem o np.float64 e o resultado. como isso? 

# %%
