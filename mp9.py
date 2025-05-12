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
date_copy = dados_copia['Date']
dados_copia['Date'] = date_copy.fillna('1900/01/01')
dados_copia['Date'] = dados_copia['Date'].str.strip()
dados_copia['Date'] = dados_copia['Date'].str.replace("'", "")
dados_copia['Date'] = dados_copia['Date'].replace('20201226', '2020/12/26')
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], errors='coerce')
print(dados_copia)
