# %%

import pandas as pd # aqui estou importando a biblioteca pandas

pd.Series() #Series como uma coluna de uma tabela

jogadores = pd.Series(["Yuri Alberto", "memphis", "Garro", "Bidon"])

# %%
print(jogadores)

#Índices:
# 0
# 1
# 2
# 3
#O pandas cria automaticamente uma identificação para cada elemento

# Os valores:

# Yuri Alberto
# Memphis
# Garro
# Bidon
# São os dados que colocamos na Series.

# Series = uma sequência de valores + índices + funcionalidades do Pandas.

# %%
idades = pd.Series([24,31,27,20])

idades.mean() #O pandas consegue calcular diretamente a média dessa Series

# %%
pd.Series()
# %%
