from datetime import datetime
import pandas as pd
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8') 
arquivo_csv = 'dados.csv'
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')
print("Primeiras 10 linhas do conjunto de dados:")
print(dados.head(10).to_string())
print("\nÚltimas 10 linhas do conjunto de dados:")
print(dados.tail(10).to_string())