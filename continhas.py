import pandas as pd
import os
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
plt.style.use("ggplot")
mpl.rcParams['figure.dpi'] = 300

def returnCategoria(regra):
    if(regra == "no-undef"):
        return "Variáveis"
    elif(regra == "no-unused-vars"):
        return "Variáveis"
    elif (regra == "no-redeclare"):
        return "Boas Práticas"
    elif (regra == "no-irregular-whitespace"):
        return "Possíveis Erros"
    elif (regra == "no-unused-labels"):
        return "Boas Práticas"
    elif (regra == "no-extra-semi"):
        return "Possíveis Erros"
    elif (regra == "no-useless-escape"):
        return "Boas Práticas"
    elif (regra == "no-constant-condition"):
        return "Possíveis Erros"
    elif (regra == "no-async-promise-executor"):
        return "Possíveis Erros"
    elif (regra == "no-case-declarations"):
        return "Boas Práticas"
    elif (regra == "no-self-assign"):
        return "Boas Práticas"
    elif (regra == "no-fallthrough"):
        return "Boas Práticas"
    elif (regra == "no-func-assign"):
        return "Possíveis Erros"
    elif (regra == "no-unreachable"):
        return "Possíveis Erros"
    elif (regra == "valid-typeof "):
        return "Possíveis Erros"

def plot_categoria_erros(dataframe):
    categorias = data['Categoria'].value_counts()
    # nomes = zip(*categorias)[0]
    # quantidades = zip(*categorias)[1]
    # x_pos = np.arange(len(nomes))
    print(categorias)
    categorias.plot.bar(rot=0)
    plt.xlabel('Categorias de Regras')
    plt.ylabel('Número de Violações')
    plt.tight_layout()
    plt.show()

def plot_regra_erros(data):
    dado = data['Regra'].value_counts()
    print(dado)
    dado.plot.bar()
    plt.xlabel('Categorias de Regras')
    plt.ylabel('Número de Violações')
    plt.tight_layout()
    plt.show()

def plot_distribuicao(dataframe):
    quantidades = dataframe['QuantidadeErros']
    quantidades.plot(kind="hist")
    print(quantidades.quantile([0.25,0.5,0.75]))
    print(quantidades.median())
    plt.xlabel('Número de Violações')
    plt.ylabel('Número de Snipets de Código')
    plt.tight_layout()
    plt.show()

def categoriasmedia(dataframe):
    gk = dataframe.groupby('Id')['Regra'].apply(list).reset_index(name='Regra')
    print(gk)
    for i in gk.index:
        gk.at[i, 'Regra'] = list(set(gk.at[i, 'Regra']))
    for i in gk.index:
        gk.at[i, 'Qtd'] = len(gk.at[i, 'Regra'])
    print(gk)

    print(gk['Qtd'].mean())
    print(gk['Qtd'].quantile([0.25,0.5,0.75]))
    print(gk['Qtd'].max())

os.chdir("./files")
data = pd.read_csv('quantidade.csv', usecols=['Id', 'Regra', 'Severidade', 'Categoria'])
data2 = pd.read_csv('erros.csv', usecols=['Id', 'QuantidadeErros'])

#print(data['Regra'].value_counts())

for i in data.index:
    data.at[i, 'Categoria'] = returnCategoria(data.at[i, 'Regra'])

plot_categoria_erros(data)
plot_regra_erros(data)
plot_distribuicao(data2)
categoriasmedia(data)