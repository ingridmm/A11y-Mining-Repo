import pandas as pd
from bs4 import BeautifulSoup

def return_only_code(body, id):
    soup = BeautifulSoup(body, features="html.parser")
    res = soup.findAll('code')
    resultado = [x.string for x in res if x.string is not None and x.string.count('\n') > 9]
    resultadoString = "\n".join(resultado)
    return resultadoString

data = pd.read_csv('results.csv')
df = data[[("<code>" in x) for x in data['body']]]

for i in df.index:
    print(i)
    df.at[i, 'body'] = return_only_code(df.at[i, 'body'], df.at[i, 'Id'])

df = df[[(x != "") for x in df['body']]]

df.to_csv("tabelafiltrada.csv", encoding='utf-8', index=False)