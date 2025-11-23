import json
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/loja_bolos"
)

def carregar_upsert():
    print("\n=== INICIANDO UPSERT MASSIVO ===")

    with open("upsert_bolos.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    sql = text("""
        INSERT INTO bolo (id_bolo, nome, preco, sabor)
        VALUES (:id_bolo, :nome, :preco, :sabor)
        ON CONFLICT (id_bolo)
        DO UPDATE SET 
            nome = EXCLUDED.nome,
            preco = EXCLUDED.preco,
            sabor = EXCLUDED.sabor;
    """)

    with engine.begin() as conn:
        for registro in dados:
            conn.execute(sql, registro)

    print("Upsert realizado com sucesso!")


def carregar_delecao():
    print("\n=== INICIANDO DELEÇÃO MASSIVA ===")

    with open("delete_bolos.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    sql_del_itens = text("DELETE FROM item_pedido WHERE bolo_id = :id_bolo")
    sql = text("DELETE FROM bolo WHERE id_bolo = :id_bolo")

    with engine.begin() as conn:
        for registro in dados:
            conn.execute(sql_del_itens, registro)
            conn.execute(sql, registro)

    print("Deleção concluída!")


def conferir_bolos():
    sql = text("SELECT * FROM bolo ORDER BY id_bolo")

    with engine.connect() as conn:
        resultado = conn.execute(sql)
        registros = resultado.fetchall()

    print("\n=== SITUAÇÃO ATUAL DA TABELA `bolo` ===")
    for linha in registros:
        print(dict(linha._mapping))


if __name__ == "__main__":
    carregar_upsert()
    conferir_bolos()

    carregar_delecao()
    conferir_bolos()
