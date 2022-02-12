Cada script disposto contribuirá para leitura e varredura de acessibilidade de snippets que contenham tags HTML e estilos em CSS.


# Projeto
1. Inicialmente faça a extração dos snippets do .csv em 'ExtractCodeFromCSV.py'. (Arquivos em html)

2. O script permitirá que o linter execute recursivamente em cada snippet -> 'eslintRunnerScript.py'. (lerá pasta com vários 'arquivo.html' para 'arquivo.csv')

3. Feita a leitura, o script permitirá que cada csv gerado da análise seja condensado em apenas um que, posteriormente será avaliado. -> 'multiple_csv_into_one.py'. ('arquivos.html' gerados para 'csv_final.csv' que formatado será 'formatado_final.csv')
 
4. No jupyter notebook permitirá que cada coluna do csv seja lida, e avaliar os resultados dos principais erros encontrado -> 'main.ipynb'. (lerá arquivo .csv gerado no passo anterior)

5. Neste mesmo notebook será possível plotar e gerar gráficos a partir do csv gerado.
