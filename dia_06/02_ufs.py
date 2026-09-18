# %% 
import pandas as pd
import requests
from io import StringIO

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

resposta = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print(resposta.status_code)
# %%
df = pd.read_html(StringIO(resposta.text))

len(df)

# %%

uf = df[1]
# %%


numero = "251 529,2"

numero = float(numero.replace(" " , "").replace(",", "."))

numero

# %%

def str_to_float(x: str):
    x = float(x.replace(" ", "").replace(",", ".").replace("\xa0", ""))
    return x 
                    
 # essa parte preciso refrescar a memoria, o replace e as aspas
        
# %%
numero = "251 529,2"

float(numero.replace(" ", "").replace(",",".")) # no primeiro (" ", "") tiro o espaço / no segundo (",", ".") eu troco a virugla pelo ponto e com isso eu crio a função para tratar as demais.


# %%

#Pelo que eu entendi se vc ja tiver convertido str pra float em uma coluna vc tem que refazer todos eles pq se não da o erro: 'float' object has no attribute 'replace'
# então tem que entrar de novo com o df pra acontecer.
uf['Área (km²)'] = uf['Área (km²)'].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
# %%

def exp_to_anos(exp:str):
    return float(exp.replace("," , ".").replace(" anos", ""))
# %%

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos) 

uf                             

# %%

def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"

    elif uf in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"

    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"

    elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"

    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"

    

# %%
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
# %%
uf[["Unidade federativa", "Região"]]

# %% 

#como aplicar apply num dataframe


#ex_01 quero exercicios desses para treinar 

# def mort_to_float(x):
#     x = x.replace("‰", "").replace(",", ".")
#     x = float(x)
#     x = x / 1000
#     return x

def mort_to_float(x):
    x = x.replace("‰", "").replace(",", ".")
    x = float(x)
    return x

uf["Mortalidade infantil (porMil)"] = uf["Mortalidade infantil (2016)"].apply(mort_to_float)
uf
# %%

#exercicio:
# Se pib / capita > 30.000 + mortalidade infantil < 15 / 1000 + IDH > 700 - > "PArece bom"
# Não parece bom

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and 
           linha ["Mortalidade infantil (porMil)"] < 15 and 
           linha ["IDH (2010)"] > 700)


# %%
uf.apply(classifica_bom, axis =1) # o que seria axis?

 
# %%

uf.apply(lambda x: x["PIB per capita (R$) (2015)"], axis= 1)