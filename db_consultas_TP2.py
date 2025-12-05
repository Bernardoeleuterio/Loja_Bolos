import psycopg2

def conectar():
    return psycopg2.connect(
        dbname="TP2_Projeto_Bloco",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

def executar_e_mostrar(titulo, query):
    print(f"\n🔎 {titulo}")
    conn = conectar()
    cur = conn.cursor()
    cur.execute(query)
    resultados = cur.fetchall()
    for linha in resultados:
        print(linha)
    cur.close()
    conn.close()

consultas = [
    ("1. Funcionários do departamento de TI", "SELECT * FROM funcionarios WHERE departamento = 'TI';"),
    ("2. Funcionários com salário > 5000", "SELECT nome FROM funcionarios WHERE REPLACE(REPLACE(salario, '.', ''), ',', '.')::numeric > 5000;"),
    ("3. Contratados após 01/01/2022", "SELECT nome, data_contratacao FROM funcionarios WHERE data_contratacao > '2022-01-01';"),
    ("4. Salário médio por departamento", "SELECT departamento, AVG(REPLACE(REPLACE(salario, '.', ''), ',', '.')::numeric) FROM funcionarios GROUP BY departamento;"),
    ("5. Nome contém 'da Silva'", "SELECT nome, cargo FROM funcionarios WHERE nome ILIKE '%da Silva%';"),
    ("6. Cargos de confiança", "SELECT * FROM funcionarios WHERE cargo_confianca = TRUE;"),
    ("7. Analistas", "SELECT nome, departamento FROM funcionarios WHERE cargo ILIKE '%analista%';"),
    ("8. Salários decrescentes", "SELECT nome, salario FROM funcionarios ORDER BY salario DESC;"),
    ("9. Contratados em 2023", "SELECT nome, id_funcionario FROM funcionarios WHERE EXTRACT(YEAR FROM data_contratacao) = 2023;"),
    ("10. Jurídico com salário até 3000", "SELECT nome FROM funcionarios WHERE departamento = 'Jurídico' AND REPLACE(REPLACE(salario, '.', ''), ',', '.')::numeric <= 3000;"),
    ("11. Gerentes ou Diretores", "SELECT nome FROM funcionarios WHERE cargo ILIKE '%gerente%' OR cargo ILIKE '%diretor%';"),
    ("12. Anos de experiência (2025)", "SELECT nome, EXTRACT(YEAR FROM AGE('2025-01-01', data_contratacao)) AS anos_experiencia FROM funcionarios;"),
    ("13. Ordenados por nome", "SELECT nome, departamento FROM funcionarios ORDER BY nome ASC;"),
    ("14. Nome começa com 'João'", "SELECT nome, cargo FROM funcionarios WHERE nome ILIKE 'João%';"),
    ("15. Quantidade por departamento", "SELECT departamento, COUNT(*) FROM funcionarios GROUP BY departamento;")
]

for titulo, query in consultas:
    executar_e_mostrar(titulo, query)
