import pandas as pd

# Lê o arquivo ODS
df = pd.read_excel("202406_CompraDireta_EmissoesAlteracoes.ods", engine="odf")

# Agrupa e conta a quantidade de passagens por órgão
qtdByOrg = df.groupby("nome_orgao_superior").size().reset_index(name="quantidade_passagens")

# Exibe o resultado
print(qtdByOrg)
