# import pandas as pd

# # Lê a planilha .ods usando o engine 'odf'
# df = pd.read_excel('', engine='odf')

# print(df.head())  # Mostra as primeiras linhas para confirmar



import pandas as pd

# Carregar a planilha
df = pd.read_excel("202406_CompraDireta_EmissoesAlteracoes.ods", engine="odf")

# Limpar os nomes das colunas
df.columns = df.columns.str.strip()

# Verificar os nomes disponíveis
print("Colunas limpas:", df.columns.tolist())

# Exemplo: mostrar valores únicos de alguma coluna real
# Aqui usamos 'situacao_bilhete' como exemplo
if 'situacao_bilhete' in df.columns:
    print("Situações encontradas:", df['situacao_bilhete'].dropna().unique())
else:
    print("Coluna 'situacao_bilhete' não encontrada.")
