# %%
valor = "45 789,50"

float(valor.replace(" ","").replace(",","."))

# %%
def converte_valor(x:str):
 return float(x.replace(" ","").replace(",","."))

# %%

converte_valor("12 500,75")
# %%

expectativa = "78,5 anos"

float(expectativa.replace(",",".").replace("anos", ""))

# %%

def converte_expectativa(x:str):
 return float(x.replace(",",".").replace("anos", ""))
# %%

converte_expectativa("81,2 anos")
# %%
def classifica_estado(estado):

    if estado in ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Espírito Santo"]:
        return "Sudeste"
    
    elif estado in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    
    elif estado in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
       return "Nordeste"
    
    elif estado in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"

    elif estado in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
       return "Sul"

    
# %%
classifica_estado("Alagoas")

# %%

classifica_estado("Paraná")
# %%

classifica_estado("Santa Catarina")

# %%
classifica_estado("Minas Gerais")

# %%
classifica_estado("Mato Grosso")

# %%

import pandas as pd

estados = pd.DataFrame({
    "estado": ["São Paulo", "Bahia", "Paraná", "Goiás"]
})
# %%

estados["Região"] = estados["estado"].apply(classifica_estado)

# %%
estados
# %%

mortalidade = "17,8‰"

float(mortalidade.replace("‰", "").replace(",","."))

# %%

pessoas = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carlos"],
    "idade": [25, 17, 32],
    "salario": [4000, 2000, 5000]
})
# %%

def  classifica_pessoa(x):
   return (
      x["idade"] >= 18
      and x["salario"] >= 3000
   )
# %%

pessoas.apply(classifica_pessoa, axis=1)

# %%

def dobro(x):
   return x * 2


# %%
dobro(10)

# %%

pessoas["salario"].apply(lambda x: x * 2)
pessoas["idade"].apply(lambda x: x + 10)

pessoas.apply(lambda x: x["salario"] + 500, axis=1)

pessoas.apply(lambda x: x["idade"]>= 18 and x["salario"]>= 3000, axis=1)