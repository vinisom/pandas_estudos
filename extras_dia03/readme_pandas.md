# 🐼 Pandas — Filtros em DataFrames

Este material reúne os principais conceitos de **filtros com Pandas**, incluindo máscaras booleanas, operadores lógicos, `isin()`, `isna()`, `notna()` e negação com `~`.

---

# 1. O que é um filtro?

Um filtro serve para selecionar somente as linhas de um DataFrame que atendem a determinada condição.

Exemplo:

```python
filtro = df["QtdePontos"] >= 50
```

Nesse caso estamos perguntando:

> Quais linhas possuem `QtdePontos` maior ou igual a 50?

O Pandas verifica a condição para **cada linha** e produz valores booleanos:

```text
True
False
True
False
...
```

* `True` → a linha atende à condição.
* `False` → a linha não atende à condição.

Essa sequência de `True` e `False` é chamada de **máscara booleana**.

---

# 2. Como um filtro funciona

Imagine:

```text
QtdePontos
10
50
100
30
80
```

Criamos:

```python
filtro = df["QtdePontos"] >= 50
```

O Pandas verifica:

```text
10 >= 50   → False
50 >= 50   → True
100 >= 50  → True
30 >= 50   → False
80 >= 50   → True
```

A variável `filtro` contém:

```text
False
True
True
False
True
```

Se executarmos:

```python
filtro
```

veremos os valores `True` e `False`.

Para aplicar o filtro:

```python
df[filtro]
```

O Pandas mantém somente as linhas correspondentes a `True`.

Resultado:

```text
QtdePontos
50
100
80
```

Portanto:

```python
filtro = df["QtdePontos"] >= 50
df[filtro]
```

pode ser entendido como:

```text
CRIAR A REGRA
     ↓
GERAR TRUE/FALSE
     ↓
APLICAR A REGRA NO DATAFRAME
     ↓
RETORNAR SOMENTE AS LINHAS TRUE
```

---

# 3. Exemplo simples com DataFrame

```python
import pandas as pd

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"],
    }
)
```

DataFrame:

| nome | idade | uf |
| ---- | ----: | -- |
| teo  |    32 | sp |
| nah  |    35 | pr |
| mah  |    14 | rj |

Queremos somente pessoas maiores de 18 anos:

```python
filtro = brinquedo["idade"] > 18
```

O filtro será:

```text
True
True
False
```

Aplicando:

```python
brinquedo[filtro]
```

Resultado:

| nome | idade | uf |
| ---- | ----: | -- |
| teo  |    32 | sp |
| nah  |    35 | pr |

---

# 4. Operadores de comparação

Os principais operadores utilizados nos filtros são:

| Operador | Significado    |
| -------- | -------------- |
| `==`     | igual          |
| `!=`     | diferente      |
| `>`      | maior          |
| `<`      | menor          |
| `>=`     | maior ou igual |
| `<=`     | menor ou igual |

Exemplos:

```python
df["QtdePontos"] == 50
```

```python
df["QtdePontos"] != 50
```

```python
df["QtdePontos"] > 50
```

```python
df["QtdePontos"] >= 50
```

```python
df["QtdePontos"] < 50
```

```python
df["QtdePontos"] <= 50
```

---

# 5. Filtros com mais de uma condição

Podemos combinar condições utilizando operadores lógicos.

Os principais são:

```text
& → E (AND)

| → OU (OR)

~ → NÃO / NEGAÇÃO (NOT)
```

---

# 6. Operador `&` — E

Exemplo:

> Quero valores maiores ou iguais a 50 E menores que 100.

```python
filtro = (
    (df["QtdePontos"] >= 50)
    &
    (df["QtdePontos"] < 100)
)

df[filtro]
```

Para uma linha ser selecionada, **as duas condições precisam ser verdadeiras**.

Tabela verdade:

| Condição A | Condição B | A & B |
| ---------- | ---------- | ----- |
| True       | True       | True  |
| True       | False      | False |
| False      | True       | False |
| False      | False      | False |

Exemplo com `70`:

```text
70 >= 50 → True
70 < 100 → True

True & True → True
```

O valor entra no resultado.

Exemplo com `120`:

```text
120 >= 50 → True
120 < 100 → False

True & False → False
```

O valor não entra.

### Regra para lembrar

> Com `&`, todas as condições precisam ser verdadeiras.

Equivalente em SQL:

```sql
WHERE QtdePontos >= 50
AND QtdePontos < 100
```

---

# 7. Operador `|` — OU

Exemplo:

> Quero valores iguais a 1 OU iguais a 100.

```python
filtro = (
    (df["QtdePontos"] == 1)
    |
    (df["QtdePontos"] == 100)
)

df[filtro]
```

Tabela verdade:

| Condição A | Condição B | A | B |
| ---------- | ---------- | ----- |
| True       | True       | True  |
| True       | False      | True  |
| False      | True       | True  |
| False      | False      | False |

Com `|`, basta **uma das condições ser verdadeira**.

Exemplo:

```text
QtdePontos = 100

100 == 1   → False
100 == 100 → True

False | True → True
```

Portanto, a linha entra.

### Regra para lembrar

> Com `|`, basta uma condição ser verdadeira.

Equivalente em SQL:

```sql
WHERE QtdePontos = 1
OR QtdePontos = 100
```

---

# 8. Misturando `&` e `|`

Exemplo:

> Pontos entre 0 e 50 OU registros criados a partir de 2025.

```python
filtro = (
    ((df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50))
    |
    (df["DtCriacao"] >= "2025-01-01")
)

df[filtro]
```

Podemos separar mentalmente:

```text
(
    pontos > 0
        E
    pontos <= 50
)

        OU

data >= 2025-01-01
```

Quando existem várias condições, utilizar parênteses deixa a lógica mais clara e evita ambiguidades.

---

# 9. `isin()`

O método:

```python
.isin()
```

verifica se cada valor está presente em uma lista de valores.

Exemplo:

```python
filtro = df["IdProduto"].isin([5, 11])
```

Significa:

> O `IdProduto` está entre os valores `5` e `11`?

Imagine:

```text
IdProduto

5
8
11
20
5
```

Resultado:

```text
5  está em [5, 11] → True
8  está em [5, 11] → False
11 está em [5, 11] → True
20 está em [5, 11] → False
5  está em [5, 11] → True
```

Podemos aplicar:

```python
filtro = df["IdProduto"].isin([5, 11])

df[filtro]
```

---

# 10. Por que utilizar `isin()`?

Poderíamos escrever:

```python
filtro = (
    (df["IdProduto"] == 5)
    |
    (df["IdProduto"] == 11)
)
```

Porém, com vários valores ficaria muito grande:

```python
filtro = (
    (df["IdProduto"] == 5)
    | (df["IdProduto"] == 11)
    | (df["IdProduto"] == 20)
    | (df["IdProduto"] == 32)
    | (df["IdProduto"] == 45)
)
```

Com `isin()`:

```python
filtro = df["IdProduto"].isin([5, 11, 20, 32, 45])
```

Muito mais simples.

Equivalente em SQL:

```sql
WHERE IdProduto IN (5, 11, 20, 32, 45)
```

---

# 11. Valores nulos

Dados reais podem possuir valores ausentes.

No Pandas, frequentemente aparecem como:

```text
NaN
```

Para verificar esses valores podemos utilizar:

```python
.isna()
```

e:

```python
.notna()
```

---

# 12. `isna()`

`isna()` verifica:

> O valor é nulo?

Exemplo:

```python
clientes["DtCriacao"].isna()
```

Imagine:

```text
DtCriacao

2025-01-10
2025-02-15
NaN
2025-04-20
NaN
```

O resultado será:

```text
2025-01-10 → False
2025-02-15 → False
NaN        → True
2025-04-20 → False
NaN        → True
```

Para selecionar somente registros onde `DtCriacao` é nulo:

```python
filtro = clientes["DtCriacao"].isna()

clientes[filtro]
```

Equivalente em SQL:

```sql
WHERE DtCriacao IS NULL
```

---

# 13. `notna()`

`notna()` verifica:

> O valor NÃO é nulo?

Exemplo:

```python
filtro = clientes["DtCriacao"].notna()

clientes[filtro]
```

Imagine:

```text
DtCriacao

2025-01-10 → True
2025-02-15 → True
NaN        → False
2025-04-20 → True
NaN        → False
```

Portanto, serão mantidas somente as linhas que possuem uma data.

Equivalente em SQL:

```sql
WHERE DtCriacao IS NOT NULL
```

---

# 14. Diferença entre `isna()` e `notna()`

| Valor          | `isna()` | `notna()` |
| -------------- | -------- | --------- |
| `"2025-01-10"` | False    | True      |
| `NaN`          | True     | False     |

Resumindo:

```text
isna()
↓
"É nulo?"

notna()
↓
"NÃO é nulo?"
```

---

# 15. Operador `~`

O operador:

```python
~
```

é utilizado para **negar/inverter uma condição booleana**.

Ele transforma:

```text
True  → False
False → True
```

Por exemplo:

```python
clientes["DtCriacao"].isna()
```

Pode produzir:

```text
False
False
True
False
True
```

Se utilizarmos:

```python
~clientes["DtCriacao"].isna()
```

teremos:

```text
True
True
False
True
False
```

Por isso:

```python
~clientes["DtCriacao"].isna()
```

possui a mesma ideia de:

```python
clientes["DtCriacao"].notna()
```

---

# 16. Comparação Pandas × SQL

Como vários conceitos são semelhantes ao SQL:

| Objetivo          | Pandas     | SQL           |
| ----------------- | ---------- | ------------- |
| Igual             | `==`       | `=`           |
| Diferente         | `!=`       | `!=` / `<>`   |
| Maior             | `>`        | `>`           |
| Menor             | `<`        | `<`           |
| Maior ou igual    | `>=`       | `>=`          |
| Menor ou igual    | `<=`       | `<=`          |
| E                 | `&`        | `AND`         |
| OU                | `\|`       | `OR`          |
| Está em uma lista | `.isin()`  | `IN`          |
| É nulo            | `.isna()`  | `IS NULL`     |
| Não é nulo        | `.notna()` | `IS NOT NULL` |
| Negação           | `~`        | `NOT`         |

---

# 17. Estrutura mental para criar filtros

Sempre pense:

```text
1. Qual DataFrame estou usando?

        ↓

2. Qual coluna quero analisar?

        ↓

3. Qual é minha condição?

        ↓

4. A condição gera True/False

        ↓

5. Aplico essa condição no DataFrame

        ↓

6. Recebo somente as linhas True
```

Exemplo:

```python
filtro = df["QtdePontos"] >= 50

df[filtro]
```

Leia como:

```text
df
↓
coluna QtdePontos
↓
é maior ou igual a 50?
↓
True / False
↓
usar isso para filtrar df
```

---

# 18. Criar filtro x aplicar filtro

Essa diferença é muito importante.

### Criando o filtro

```python
filtro = brinquedo["idade"] > 18
```

Aqui estamos criando a condição.

A variável `filtro` recebe uma Series de:

```text
True
True
False
...
```

### Visualizando o filtro

```python
filtro
```

Mostra os booleanos.

### Aplicando o filtro

```python
brinquedo[filtro]
```

Mostra o DataFrame somente com as linhas onde o filtro é `True`.

Portanto:

```text
filtro
```

não é a tabela filtrada.

Ele é a **máscara utilizada para filtrar a tabela**.

---

# 19. Forma direta

Também é possível fazer:

```python
brinquedo[brinquedo["idade"] > 18]
```

Em vez de:

```python
filtro = brinquedo["idade"] > 18

brinquedo[filtro]
```

As duas formas funcionam.

Durante os estudos, separar em:

```python
filtro = ...
df[filtro]
```

pode facilitar a compreensão.

---

# 20. Resumo rápido

### Filtro simples

```python
filtro = df["QtdePontos"] >= 50

df[filtro]
```

### Duas condições com E

```python
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)

df[filtro]
```

### Duas condições com OU

```python
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)

df[filtro]
```

### Verificar vários valores

```python
filtro = df["IdProduto"].isin([5, 11])

df[filtro]
```

### Procurar valores nulos

```python
filtro = clientes["DtCriacao"].isna()

clientes[filtro]
```

### Procurar valores não nulos

```python
filtro = clientes["DtCriacao"].notna()

clientes[filtro]
```

### Negar uma condição

```python
filtro = ~clientes["DtCriacao"].isna()

clientes[filtro]
```

---

# 🧠 Conceito principal

O ponto mais importante para entender filtros no Pandas é:

> **Uma condição aplicada a uma Series gera uma sequência de valores `True` e `False`. Essa sequência é chamada de máscara booleana. Quando usamos essa máscara dentro de `df[filtro]`, o Pandas mantém as linhas `True` e descarta as linhas `False`.**

Fluxo:

```text
DATAFRAME
    ↓
ESCOLHER COLUNA
    ↓
CRIAR CONDIÇÃO
    ↓
TRUE / FALSE
    ↓
MÁSCARA BOOLEANA
    ↓
df[filtro]
    ↓
DATAFRAME FILTRADO
```
