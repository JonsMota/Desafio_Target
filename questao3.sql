-- Criar a tabela de faturamento
CREATE TABLE faturamento_diario (
    dia INT,
    valor DECIMAL(10, 2)
);

-- Inserir os dados de faturamento
INSERT INTO faturamento_diario (dia, valor) VALUES
(1, 100.00),
(2, 200.00),
(3, 0.00), -- Dia sem faturamento
(4, 300.00),
(5, 400.00);

-- Calcular o menor valor de faturamento
CREATE TEMP VIEW menor_valor AS
SELECT MIN(valor) AS menor_valor
FROM faturamento_diario
WHERE valor > 0;

-- Calcular o maior valor de faturamento
CREATE TEMP VIEW maior_valor AS
SELECT MAX(valor) AS maior_valor
FROM faturamento_diario
WHERE valor > 0;

-- Calcular a média mensal, ignorando dias sem faturamento
CREATE TEMP VIEW media_mensal AS
SELECT AVG(valor) AS media_mensal
FROM faturamento_diario
WHERE valor > 0;

-- Contar o número de dias com faturamento acima da média
CREATE TEMP VIEW dias_acima_da_media AS
WITH media AS (
    SELECT AVG(valor) AS media_mensal
    FROM faturamento_diario
    WHERE valor > 0
)
SELECT COUNT(*) AS dias_acima_da_media
FROM faturamento_diario, media
WHERE faturamento_diario.valor > media.media_mensal;

-- Selecionar os resultados
SELECT * FROM menor_valor;
SELECT * FROM maior_valor;
SELECT * FROM media_mensal;
SELECT * FROM dias_acima_da_media;