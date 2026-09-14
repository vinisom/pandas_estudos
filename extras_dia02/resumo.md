# 📂 Pandas — Leitura e Salvamento de Arquivos

## 🔄 Fluxo básico

ARQUIVO → PANDAS → DATAFRAME → PANDAS → ARQUIVO

Exemplo:

clientes.csv
     ↓
pd.read_csv()
     ↓
DataFrame
     ↓
tratamento/análise
     ↓
df.to_csv()
     ↓
novo_arquivo.csv


QUERO ABRIR/LER UM ARQUIVO?
        ↓
      read
        ↓
pd.read_csv()
pd.read_excel()
pd.read_parquet()


QUERO SALVAR UM DATAFRAME?
        ↓
       to
        ↓
df.to_csv()
df.to_excel()
df.to_parquet()


O principal para você consultar rapidamente é esta associação:

**`read` = arquivo → DataFrame**

**`to` = DataFrame → arquivo**

E `index=False` = **não quero levar o índice para o arquivo salvo**.

