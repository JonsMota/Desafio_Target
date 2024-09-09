-- Criar a tabela de faturamento por estado
CREATE TABLE faturamento_estados (
    estado VARCHAR(2),
    valor DECIMAL(10, 2)
);

-- Inserir os dados de faturamento
INSERT INTO faturamento_estados (estado, valor) VALUES
('SP', 67836.43),
('RJ', 36678.66),
('MG', 29229.88),
('ES', 27165.48),
('Outros', 19849.53);

-- Calcular o faturamento total
CREATE TEMP VIEW faturamento_total AS
SELECT SUM(valor) AS total
FROM faturamento_estados;

-- Calcular o percentual de cada estado
CREATE TEMP VIEW percentual_estados AS
SELECT estado, (valor / (SELECT total FROM faturamento_total) * 100) AS percentual
FROM faturamento_estados;

-- Selecionar os resultados
SELECT * FROM percentual_estados;