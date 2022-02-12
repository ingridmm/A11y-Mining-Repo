import os
import glob
import pandas as pd

#seta o local
path = "/home/ingridmoreira/Documentos/Arquivos_Finais"

#listar .csv de diretório
#percorre diretório -> 'glob'
#salva na lista -> all_filenames
all_filenames = [i for i in glob.glob(path + "/*.csv")]
#print(all_filenames)

#combina todos os .csv do diretório em um só
df = [pd.read_csv(f, header=None, sep='delimiter', engine='python') for f in all_filenames]
combined_csv = pd.concat(df)

#na exportação nome pode ser modificado
combined_csv.to_csv( "csv_final.csv", index=False, encoding='utf-8-sig')
