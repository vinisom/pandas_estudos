# %%

import pandas as pd
# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %%

filtro = clientes["qtdePontos"] == 0

clientes_0 = clientes[filtro] #atribuição certo?

clientes_0["Flag_1"] = 1



#ele nao faz uma cópia, ele faz uma view. falou que é um ponteiro.
#ele diz que no python tudo é ponteiro, tudo é referência!


# %%

A = [1,2]
B = A

print("A: ", A)
print("B: ", B)

B.append("teste")

print("A: ", A)
print("B: ", B)

#AS variaveis em pyhton não são gavetas e sim post-it

# %%

A = [1,2]
B = A.copy()
print("A: ", A)
print("B: ", B)

B.append("teste")
print("A: ", A)
print("B: ", B)

# %%

filtro = clientes["qtdePontos"] == 0

clientes_0 = clientes[filtro].copy()

clientes_0["Flag_1"] = 1

# %%
clientes_0