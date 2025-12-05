from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/loja_bolos")

QUERY_INNER = """
SELECT c.nome AS cliente,
       b.nome AS bolo,
       ip.quantidade,
       ip.preco_unitario,
       p.data_pedido
FROM item_pedido ip
INNER JOIN pedido p ON ip.pedido_id = p.id_pedido
INNER JOIN cliente c ON p.cliente_id = c.id_cliente
INNER JOIN bolo b ON ip.bolo_id = b.id_bolo;
"""

QUERY_LEFT = """
SELECT c.nome AS cliente,
       p.id_pedido,
       p.total
FROM cliente c
LEFT JOIN pedido p ON c.id_cliente = p.cliente_id;
"""

QUERY_RIGHT = """
SELECT p.id_pedido,
       c.nome AS cliente,
       p.total
FROM cliente c
RIGHT JOIN pedido p ON c.id_cliente = p.cliente_id;
"""

def executar_consulta_dicionario(sql):
    with engine.connect() as conexao:
        resultado = conexao.execute(text(sql))
        linhas = [dict(linha._mapping) for linha in resultado]
    return linhas

def imprimir_dicionarios():
    print("\n=== RESULTADO INNER JOIN ===")
    for linha in executar_consulta_dicionario(QUERY_INNER):
        print(linha)

    print("\n=== RESULTADO LEFT JOIN ===")
    for linha in executar_consulta_dicionario(QUERY_LEFT):
        print(linha)

    print("\n=== RESULTADO RIGHT JOIN ===")
    for linha in executar_consulta_dicionario(QUERY_RIGHT):
        print(linha)

def executar_consulta_lista(sql):
    with engine.connect() as conexao:
        resultado = conexao.execute(text(sql))
        linhas = [tuple(linha) for linha in resultado]
    return linhas

def imprimir_listas():
    print("\n=== RESULTADO INNER JOIN (LISTAS) ===")
    for linha in executar_consulta_lista(QUERY_INNER):
        print(linha)

    print("\n=== RESULTADO LEFT JOIN (LISTAS) ===")
    for linha in executar_consulta_lista(QUERY_LEFT):
        print(linha)

    print("\n=== RESULTADO RIGHT JOIN (LISTAS) ===")
    for linha in executar_consulta_lista(QUERY_RIGHT):
        print(linha)

if __name__ == "__main__":
    print(">> CONECTANDO AO BANCO loja_bolos ...")
    try:
        imprimir_dicionarios()
        imprimir_listas()
        print("\n Consultas executadas com sucesso!")
    except Exception as e:
        print(f"\n Erro ao executar consultas: {e}")
