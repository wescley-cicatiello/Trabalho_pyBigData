import pandas as pd

# lê o arquivo ODS
df = pd.read_excel("202406_CompraDireta_EmissoesAlteracoes.ods", engine="odf")

#Garante que a coluna valor_bilhete é numérica
df["valor_bilhete"] = pd.to_numeric(df["valor_bilhete"], errors="coerce")

# agrupa por orgão e soma os valores dos bilhetes
soma_bilhetes = df.groupby("nome_orgao_superior")["valor_bilhete"].sum().reset_index()

#renomeia a coluna de resultado
soma_bilhetes = soma_bilhetes.rename(columns={"valor_bilhete": "total_gasto_bilhete"})

# Formata os valores como R$ 1.234,56
soma_bilhetes["total_gasto_bilhete"] = soma_bilhetes["total_gasto_bilhete"].apply(
    lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)

#exibe resultado
print(soma_bilhetes)
