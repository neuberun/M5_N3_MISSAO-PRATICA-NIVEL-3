from datetime import datetime
import pandas as pd
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8') 
arquivo_csv = 'dados.csv'
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')
dados_copia = dados.copy()
print(dados_copia)