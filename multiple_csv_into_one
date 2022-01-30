import os
import glob
import pandas as pd
#set working directory
path = "/home/ingridmoreira/Documentos/csv_test"

#find all csv files in the folder
#use glob pattern matching -> extension = 'csv'
#save result in list -> all_filenames
#extension = 'csv'
all_filenames = [i for i in glob.glob(path + "/*.csv")]
#print(all_filenames)

#combine all files in the list
df = [pd.read_csv(f, header=None, sep='delimiter', engine='python') for f in all_filenames]
combined_csv = pd.concat(df)
#export to csv
combined_csv.to_csv( "csv_final.csv", index=False, encoding='utf-8-sig')
