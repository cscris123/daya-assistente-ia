# Base de Conhecimento — SQL e Banco de Dados

## Conceitos
- **SELECT:** seleciona colunas.
- **WHERE:** filtra registros.
- **GROUP BY:** agrupa registros para agregações.
- **Agregações:** `COUNT`, `SUM`, `AVG`, `MIN` e `MAX`.
- **JOIN:** combina registros de tabelas relacionadas.
- **Chave primária:** identifica unicamente um registro.
- **Chave estrangeira:** representa uma relação com outra tabela.

## Exemplo
```sql
SELECT categoria, COUNT(*) AS quantidade
FROM produtos
GROUP BY categoria;
```

## Boas práticas
Evitar `SELECT *` quando não for necessário, usar nomes claros e validar filtros e junções.

## Aprofundamento
Índices, normalização, CTEs, subqueries, funções de janela, planos de execução e otimização.
