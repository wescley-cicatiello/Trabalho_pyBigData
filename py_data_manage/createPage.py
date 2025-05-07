import pandas as pd

# Lê a planilha .ods usando o engine 'odf'
df = pd.read_excel('', engine='odf')

print(df.head())  # Mostra as primeiras linhas para confirmar
