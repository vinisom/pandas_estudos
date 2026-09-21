# %%

codigo = "BRA-SP-SANTOANDRE-2026"

codigo = codigo.split("-")[-1]
codigo


# %%

produto = "CAMISETA;AZUL;GG;159"

produto.split(";")[-1]

# %%

def get_produto(x):
   return x.split(";")[-1]
    


# %%

import pandas as pd

df_produtos = pd.DataFrame({
    "produto": [
        "CAMISETA;AZUL;GG;159",
        "TENIS;PRETO;42;399",
        "BONE;BRANCO;M;89"
    ]
})
# %%

def _get_preco(x):
   return x.split(";")[-1]
# %%

df_produtos["produto"].apply(_get_preco)

# %%

df_codigos = pd.DataFrame({
    "codigo": [
        "BR-SP-2026",
        "BR-RJ-2025",
        "BR-MG-2024"
    ]
})


# %%
def get_ano(x):
   return x.split("-")[-1]
# %%
df_codigos["ano"] = df_codigos["codigo"].apply(get_ano)
# %%
df_codigos
# %%
