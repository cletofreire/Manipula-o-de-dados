#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando as bibliotecas necessárias 
import pandas as pd
import missingno
import numpy as np


# In[2]:


# Abrindo o arquivo
file = 'country_vaccinations.csv'
df = pd.read_csv (file)


# In[3]:


# Lendo as primeiras 10  linhas da tabela
df.head(10)


# In[4]:


# Lendo os últimas 10  linhas da tabela

df.tail(10)


# In[5]:


#Observando se há valores faltantes de caráter observacional, onde há o menor N amostral por coluna observa-se a ausência de amostras
df.info()


# In[6]:


# De maneira objetiva esse comando nos mostra as colunas que há valores faltantes , sendo  FALSE para as COLUNAS que NÃO tem valores faltantes e TRUE para os que TEM valores faltantes
df.isna().any()


# In[7]:


# Observando por meio de  de uma interface gráfica de maneira precisa onde  há os valores faltantes
#Obs: Os espaços em branco correspondem aos valores faltantes
missingno.matrix(df)


# In[15]:


# É um gráfico de barras ilustra os valores totais de todas as colunas
missingno.bar(df)


# In[8]:


# Aqui ele vai me retornar todas as linhas que possui pelo menos um valor faltante (isna().any)
df[df.isna().any(axis = 1)] 


# In[18]:


# Me retorna linhas  que não tem nenhum valor faltante, observe que agora = notna(). all
# em suma elimina os n/as

df[df.notna().all(axis = 1)]  


# In[9]:


# Aqui com o comando reset_index, eu reseto os valores naturais da ordem do data frame e mantenho apenas as amostras que estão presentes em todas as linhas e colunas
# OBS: Deixei de lado/joguei  fora todos os dados faltantes

df2 = df[df.notna().all(axis = 1)]. reset_index(drop = True)


# In[14]:


# Observe que todas as colunas possuem a mesma quantidade de amostras 
df2.info()


# In[13]:


# Observando graficamente (2), note que não há lacunas, tudo preenchidos sem espaços em branco
missingno.matrix(df2)


# In[17]:


# Aqui calculamos a porcentagem por meio do laço de repetição (for) dos valores faltantes.
for col in df.columns:
    perc = np.mean(df[col].isna())
    print (f'{col}: {round(perc*100)} %')


# In[ ]:


# Selecionei a coluna total vacinations e dentro dela só quero os que são menores ou iguais a dez mil

dff = df[df['total_vaccinations'] <=10000]
dff.info()


# In[19]:


# Esta função é análoga a de cima, a partir de então irei usa-la.

dff2 = df.query('total_vaccinations <=10000')
dff2


# In[20]:


# Na coluna country eu selecionei o Brazil e na coluna people vaccinated os que estão acima de 100000 (cem mil)
dff3 = df.query('country == "Brazil" & people_vaccinated >= 100000')
dff3


# In[23]:


# OU no formato de  | , aqui ele irá selecionar todos as linhas que possuem mais de 1 mihção na coluna total vaccinations ou as linhas que tem mais de cem mil na coluna people fully vaccination
dff4 = df.query ('total_vaccinations > 1e6 | people_fully_vaccinated > 1e5')
dff4


# In[ ]:


# Filtrando data específica e nação
df.query('date >= " 2021-06-01" & country == "Afghanistan"')


# In[ ]:


# FILTRANDO INTERVALOS DE TEMPO entre dia 01 e dia 31
df.query ('date in ["2021-05-01", "2021-05-31"]')


# In[25]:


# ELIMINANDO as colunas que possuem  N/AS nas colunas
dff5= df.dropna(axis=1)
dff5


# In[29]:


# Substituindo N/AS pela mediana
#Calculado a mediana
dfm= df.median()
dfm


# In[30]:


# listando os valores
mediana = df.median().values
mediana


# In[32]:


#Selecionando as colunas com valores numéricos
cols = ['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'daily_vaccinations_raw', 'daily_vaccinations', 'total_vaccinations_per_hundred','people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred','daily_vaccinations_per_million']
len(cols)


# In[33]:


#substituindo os valores faltantes pela mediana de cada coluna
for i in range(len(mediana)):
    df[cols[i]] = df[cols[i]].fillna(mediana[i])


# In[34]:


#Conferindo, todos as colunas possuem a mesma quantidade de 
df.info()


# In[35]:


# Observando graficamente
missingno.matrix(df)


# In[ ]:




