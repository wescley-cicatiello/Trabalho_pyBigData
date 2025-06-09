import pandas as pd

# Lê o arquivo .ods
df = pd.read_excel("202406_CompraDireta_EmissoesAlteracoes.ods", engine="odf")

# Agrupa por companhia aérea e conta as passagens
passagens_por_companhia = df.groupby("companhia_aerea").size().reset_index(name="quantidade_passagens")

# Ordena do maior para o menor
passagens_por_companhia = passagens_por_companhia.sort_values(by="quantidade_passagens", ascending=False)

# Exibe o resultado
print(passagens_por_companhia)
