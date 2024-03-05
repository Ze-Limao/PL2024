# TPC4: Analisador Léxico para queries SQL
#### Autor: José Afonso Lopes Correia, A100610  

## Resumo:
Este programa consiste num analisador léxico que consigue identificar e classificar os tokens de uma expressão SQL.

Para tal, o programa deverá ser capaz de identificar os seguintes tokens:

- Comandos SQL: `SELECT`, `INSERT INTO`, `UPDATE`, `DELETE FROM`, `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE`;
- Nomes de objetos;
- Números;
- Delimitadores: `(`, `)`, `,`;
- Delimitadores finais: `;`;
- Operadores matemáticos: `=`, `<>`, `!=`, `>`, `<`, `>=`, `<=`, `+`, `-`, `*`, `/`;
- Operadores SQL: `AND`, `OR`, `NOT`, `IN`;

Recorreu-se à biblioteca [ply](https://www.dabeaz.com/ply/ply.html), uma ferramenta para a construção de analisadores léxicos e sintáticos.