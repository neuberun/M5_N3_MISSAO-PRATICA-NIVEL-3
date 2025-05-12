from datetime import datetime
import pandas as pd
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8') 
arquivo_csv = 'dados.csv'
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')
dados_copia = dados.copy()
calories_copy = dados_copia['Calories']
dados_copia['Calories'] = calories_copy.fillna(0)
print(dados_copia)