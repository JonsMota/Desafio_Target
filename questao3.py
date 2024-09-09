import json

# Carregar os dados do arquivo JSON
with open('faturamento.json') as f:
    data = json.load(f)

# Filtrar os valores de faturamento, excluindo dias sem faturamento
faturamento = [dia['valor'] for dia in data if dia['valor'] > 0]

# Calcular o menor e o maior valor de faturamento
menor_valor = min(faturamento)
maior_valor = max(faturamento)

# Calcular a média mensal de faturamento
media_mensal = sum(faturamento) / len(faturamento)

# Contar o número de dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

# Imprimir os resultados
print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")