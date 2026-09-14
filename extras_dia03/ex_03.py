# %%

# REFERÊNCIA E CÓPIA EM PYTHON

# Variáveis em Python podem ser entendidas como nomes
# que fazem referência a objetos.

# B = A
# → não cria automaticamente uma cópia.
# → B passa a referenciar o mesmo objeto que A.

# B = A.copy()
# → cria uma cópia.
# → A e B passam a referenciar objetos diferentes.

# No Pandas, quando quero obter um subconjunto de um
# DataFrame e modificá-lo de forma independente:

# filtro = clientes["qtdePontos"] == 0

# clientes_0 = clientes[filtro].copy()

# clientes_0["Flag_1"] = 1


a = [1,2]
b = a

print( a is b)

# %%

a = [1,2]
b = a.copy()

print(a is b)

# %%

a = [10,20]

b = a
b.append(30)

print("A:", a)

print("B;", b)

# %%

a = [10,20]

b = a.copy()

b.append(30)

print("A:", a)

print("B;", b)


# %%
#a
jogadores = ["Yuri", "Garro"]

#b
lista_2 = jogadores

lista_2.append("Hugo Neneca")

jogadores.append("Memphis")

print("Jogadores:", jogadores)
print("Lista_2", lista_2)

# %%

A = [1, 2]
B = A

print(A is B)
print(A == B)
# %%
A = [1, 2]
B = A.copy()

print(A)
print(B)