import sqlite3

def run_script(script_path):
    with open(script_path, 'r') as file:
        script = file.read()
    
    conn = sqlite3.connect(':memory:')  # Usar um banco de dados em memória
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    
    # Executar e imprimir os resultados das consultas
    print("Menor valor de faturamento:")
    for row in cursor.execute("SELECT * FROM menor_valor"):
        print(row)
    
    print("\nMaior valor de faturamento:")
    for row in cursor.execute("SELECT * FROM maior_valor"):
        print(row)
    
    print("\nMédia mensal de faturamento:")
    for row in cursor.execute("SELECT * FROM media_mensal"):
        print(row)
    
    print("\nDias com faturamento acima da média:")
    for row in cursor.execute("SELECT * FROM dias_acima_da_media"):
        print(row)
    
    conn.close()

# Executar o script SQL
run_script('questao3.sql')