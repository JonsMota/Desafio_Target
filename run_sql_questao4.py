import sqlite3

def run_script(script_path):
    with open(script_path, 'r') as file:
        script = file.read()
    
    conn = sqlite3.connect(':memory:')  # Usar um banco de dados em memória
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    
    # Executar e imprimir os resultados das consultas
    print("Percentual de faturamento por estado:")
    for row in cursor.execute("SELECT * FROM percentual_estados"):
        print(f"Estado: {row[0]}, Percentual: {row[1]:.2f}%")
    
    conn.close()

# Executar o script SQL
run_script('questao4.sql')