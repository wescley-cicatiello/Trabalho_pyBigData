import pandas as pd

# Lê o arquivo .ods
df = pd.read_excel("202406_CompraDireta_EmissoesAlteracoes.ods", engine="odf")

# Garante que a coluna 'valor_bilhete' seja numérica
df["valor_bilhete"] = pd.to_numeric(df["valor_bilhete"], errors="coerce")

# Agrupa por companhia aérea e soma os valores dos bilhetes
soma_por_companhia = df.groupby("companhia_aerea")["valor_bilhete"].sum().reset_index()

# Renomeia a coluna com o resultado
soma_por_companhia = soma_por_companhia.rename(columns={"valor_bilhete": "total_gasto_bilhetes"})

# Formata os valores como R$ 1.234,56
soma_por_companhia["total_gasto_bilhetes"] = soma_por_companhia["total_gasto_bilhetes"].apply(
    lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)

# Ordena do maior para o menor
soma_por_companhia = soma_por_companhia.sort_values(by="total_gasto_bilhetes", ascending=False)

# Exibe o resultado
print(soma_por_companhia)
