# %%
import pandas as pd
import sqlalchemy 
# %%
engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")


# %%
clientes = pd.read_sql_table(table_name="tb_customers",con=engine) #de exemplo de ORM
# %%

clientes.shape

# %%

query = "SELECT * FROM tb_customers LIMIT 100"

df_100 = pd.read_sql_query(query, con=engine)
df_100


# %%

query = "SELECT * FROM tb_orders LIMIT 100"

df_100 = pd.read_sql_query(query, con=engine)
df_100