# %%
import pandas as pd
import sqlalchemy

# from sklearn import cluster

# %%

with open("etl.sql") as open_file:
    query = open_file.read()

print(query)

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")
df = pd.read_sql_query(query, con=engine)
df

# %%

# kmean = cluster.KMeans(n_clusters=4)
# kmean.fit(df[['TotalRevenue','qtSalles']])

# df.to_sql("sellers_cluster", con=engine, index=False)

#tudo que comentei é o que eu vou aprender em