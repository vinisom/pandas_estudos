# 🐼 Estudos de Pandas

Este repositório reúne meus estudos e exercícios práticos de **Pandas**, biblioteca Python utilizada para manipulação, tratamento e análise de dados.

O objetivo é registrar minha evolução no aprendizado da biblioteca, desde a criação e manipulação de **Series e DataFrames** até técnicas de limpeza, transformação e exploração de dados.

## 📚 Conteúdos estudados

### Series

* Criação de Series com `pd.Series()`
* Índices e valores
* Acesso aos dados
* Ordenação com `sort_values()`
* Cálculos estatísticos
* Média com `mean()`
* Variância com `var()`

### Indexação com `loc` e `iloc`

Estudo das diferentes formas de acessar informações dentro de Series e DataFrames.

* `loc` → acesso utilizando **rótulos/índices**
* `iloc` → acesso utilizando **posição**

Exemplos:

```python
df.loc[0]
df.loc[0]["nome"]

df.iloc[0]
df.iloc[-1]
df.iloc[-1]["idade"]
```

Também foram praticados conceitos como:

```python
df.iloc[::-1]
```

para acessar os dados em ordem inversa.

## 📊 DataFrames

Criação e manipulação de DataFrames utilizando:

```python
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Julia"],
    "idade": [25, 30, 28]
}

df = pd.DataFrame(dados)
```

Principais conceitos estudados:

* Linhas e colunas
* Índices
* Seleção de colunas
* Seleção de linhas
* Acesso a valores específicos
* Estrutura de um DataFrame

## 🔎 Exploração dos dados

Métodos e atributos utilizados para conhecer um conjunto de dados:

```python
df.head()
df.tail()
df.sample()
df.info()

df.shape
df.columns
df.index
```

Também foi estudada a diferença entre **métodos** e **atributos** no Pandas.

Exemplo:

```python
df.head()   # método
df.shape    # atributo
```

## 💾 Leitura e exportação de arquivos

Prática com diferentes formatos de arquivos.

### CSV

```python
df.to_csv("clientes.csv", index=False)

df = pd.read_csv("clientes.csv")
```

Para arquivos separados por `;`:

```python
df = pd.read_csv("clientes.csv", sep=";")
```

### Excel

```python
df.to_excel("clientes.xlsx", index=False)

df = pd.read_excel("clientes.xlsx")
```

### Parquet

```python
df.to_parquet("clientes.parquet", index=False)

df = pd.read_parquet("clientes.parquet")
```

## 🧹 Tratamento de valores ausentes

Identificação e tratamento de valores nulos dentro de DataFrames.

### Removendo valores ausentes

```python
df.dropna()
```

Removendo linhas de acordo com diferentes condições:

```python
df.dropna(how="any")
df.dropna(how="all")
```

Utilizando colunas específicas:

```python
df.dropna(subset=["idade"])
```

### Preenchendo valores ausentes

Utilização do `fillna()`:

```python
df["salario"].fillna(0)
```

Também é possível definir valores diferentes para cada coluna:

```python
df.fillna({
    "nome": "Desconhecido",
    "salario": 0
})
```

Preenchimento utilizando a média:

```python
medias = df[["idade", "salario"]].mean()

df.fillna(medias)
```

## 🧠 Conceitos importantes

Durante os estudos, alguns conceitos fundamentais foram trabalhados:

**Índice x posição**

O índice é o identificador associado à linha do DataFrame, enquanto a posição representa onde aquela linha está localizada na estrutura.

**`loc` x `iloc`**

```python
df.loc[0]
```

Busca utilizando o **índice/rótulo**.

```python
df.iloc[0]
```

Busca utilizando a **posição**.

**`index=False`**

Ao exportar um DataFrame:

```python
df.to_csv("dados.csv", index=False)
```

o `index=False` impede que o índice do Pandas seja salvo como uma coluna adicional no arquivo.

## 🎯 Objetivo dos estudos

O objetivo deste repositório é desenvolver uma base sólida em Pandas para aplicação em projetos de **Análise de Dados e Engenharia de Dados**, principalmente nas etapas de:

* Importação de dados
* Exploração
* Limpeza
* Tratamento
* Transformação
* Preparação dos dados para análise
* Integração com bancos de dados e outras ferramentas

## 🛠️ Tecnologias utilizadas

* Python
* Pandas
* Jupyter Notebook / VS Code
* CSV
* Excel
* Parquet

## 📈 Em evolução

Este repositório será atualizado conforme avanço nos estudos de Pandas, adicionando novos conceitos, exercícios e aplicações práticas.

Entre os próximos conteúdos estão técnicas mais avançadas de manipulação, transformação, agrupamento e análise de dados.
