# A11y Data Mining

Cada script disposto contribuirá para leitura e varredura de acessibilidade segundo diretrizes do WCAG 2.0 em snippets que contenham tags HTML e estilos em CSS.

## Instruções para execução do projeto

1. Inicialmente faça a extração dos snippets do .csv em 'ExtractCodeFromCSV.py', ficando a critério do usuário o formato a ser salvo, .html, .txt e etc.

2. O script permitirá que o linter execute recursivamente em cada snippet -> 'eslintRunnerScript.py';

3. Feita a leitura, o script permitirá que cada csv gerado da análise seja condensado em apenas um que, posteriormente será avaliado. -> 'multiple_csv_into_one.py';
 
4. No jupyter notebook permitirá que cada coluna do csv seja lida, e avaliar os resultados dos principais erros encontrado -> 'rulesCounter.ipynb';

5. Neste mesmo notebook será possível plotar e gerar gráficos a partir do .csv gerado.
