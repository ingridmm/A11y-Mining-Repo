import glob
import os
import json
import csv
import pandas as pd


def parse_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.loads(file.read())

def salvar_quantidades_erros(lista):
    listaSaida = []
    listaPorArquivo = []
    for report in lista:
        for file in report:
            evitar = False
            lista_erros = file['messages']
            for erro in lista_erros:
                if(erro['ruleId'] is not None):
                    listaSaida.append([(file['filePath'])[-11:-3], erro['ruleId'], erro['severity']])
                else:
                    evitar = True

            if(not evitar):
                listaPorArquivo.append([(file['filePath'])[-11:-3], file['errorCount']])

    df = pd.DataFrame(listaSaida, columns=['Id', 'Regra', 'Severidade'])
    df2 = pd.DataFrame(listaPorArquivo, columns=['Id', 'QuantidadeErros'])
    df.to_csv('quantidade.csv', index=False)
    df2.to_csv('erros.csv', index=False)

os.chdir("./files")
fileDir = glob.glob('report*.json')
l = []

for idx, x in enumerate(fileDir):
    print("Reading json Reports{}...".format(idx))
    l.append(parse_json(x))

salvar_quantidades_erros(l)
