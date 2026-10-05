# %%
import pandas as pd

df = pd.read_csv("homicidios_consolidado.csv", sep=";")
df.head()

# %%

df_stack = (df.set_index(["nome", "período"])
            .stack()
            .reset_index())

df_stack.columns = ["nome", "período", "metrica", "valor"]

# %%

df_stack.pivot_table(values="valor",
                    index=["nome", "período"],
                    columns="metrica")

# %%

(df_stack.pivot_table(
    values="valor",
    index=["nome", "período"],
    columns="metrica")
 .reset_index())

# %%

df_stack.pivot_table(values="valor",
                index=["nome"],
                columns="metrica",
                aggfunc='mean'
                )

# %%

df_stack.pivot_table(values="valor",
                index=["nome"],
                columns="metrica",
                aggfunc='max'
                )
# %%
df_stack.pivot_table(values="valor",
                index=["nome"],
                columns="metrica",
                aggfunc='min'
                )
# %%

#se eu quiser fazer ao contrário

(df_stack.pivot_table(
    values="valor",
    index=["nome", "período"],
    columns="metrica"
)
.stack()
)
# %%
