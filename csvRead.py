import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_excel('202406_CompraDireta_EmissoesAlteracoes.ods')

# Exibe como uma tabela
print(df)
