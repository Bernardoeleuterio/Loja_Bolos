from sqlalchemy import create_engine, text


engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/loja_bolos"
)

with engine.begin() as conexao:

    conexao.execute(text("""
        INSERT INTO cliente (id_cliente, nome, email, telefone) VALUES
        (1, 'Ana Silva', 'ana@email.com', '(11) 90000-0001'),
        (2, 'Bruno Costa', 'bruno@email.com', '(11) 90000-0002'),
        (3, 'Carlos Lima', 'carlos@email.com', '(11) 90000-0003'),
        (4, 'Daniela Souza', 'daniela@email.com', '(11) 90000-0004'),
        (5, 'Eduardo Rocha', 'eduardo@email.com', '(11) 90000-0005'),
        (6, 'Fernanda Alves', 'fernanda@email.com', '(11) 90000-0006'),
        (7, 'Gabriel Pires', 'gabriel@email.com', '(11) 90000-0007'),
        (8, 'Helena Martins', 'helena@email.com', '(11) 90000-0008'),
        (9, 'Igor Teixeira', 'igor@email.com', '(11) 90000-0009'),
        (10, 'Juliana Moraes', 'juliana@email.com', '(11) 90000-0010');
    """))

    conexao.execute(text("""
        INSERT INTO bolo (id_bolo, nome, sabor, preco) VALUES
        (1, 'Bolo de Chocolate', 'Chocolate', 35.50),
        (2, 'Bolo de Morango', 'Morango', 32.00),
        (3, 'Bolo de Cenoura', 'Cenoura', 30.00),
        (4, 'Bolo de Coco', 'Coco', 28.00),
        (5, 'Bolo de Limão', 'Limão', 27.50),
        (6, 'Bolo de Laranja', 'Laranja', 26.00),
        (7, 'Bolo Red Velvet', 'Red Velvet', 40.00),
        (8, 'Bolo de Nozes', 'Nozes', 45.00),
        (9, 'Bolo de Baunilha', 'Baunilha', 25.00),
        (10, 'Bolo Prestígio', 'Chocolate/Coco', 38.00);
    """))

    conexao.execute(text("""
        INSERT INTO pedido (id_pedido, cliente_id, data_pedido, total) VALUES
        (1, 1, '2025-01-01', 71.00),
        (2, 2, '2025-01-02', 32.00),
        (3, 3, '2025-01-03', 60.00),
        (4, 4, '2025-01-04', 28.00),
        (5, 5, '2025-01-05', 40.00),
        (6, 6, '2025-01-06', 45.00),
        (7, 7, '2025-01-07', 35.50),
        (8, 8, '2025-01-08', 27.50),
        (9, 9, '2025-01-09', 26.00),
        (10, 10, '2025-01-10', 38.00);
    """))

    conexao.execute(text("""
        INSERT INTO item_pedido (id_item, pedido_id, bolo_id, quantidade, preco_unitario) VALUES
        (1, 1, 1, 2, 35.50),
        (2, 2, 2, 1, 32.00),
        (3, 3, 3, 2, 30.00),
        (4, 4, 4, 1, 28.00),
        (5, 5, 7, 1, 40.00),
        (6, 6, 8, 1, 45.00),
        (7, 7, 1, 1, 35.50),
        (8, 8, 5, 1, 27.50),
        (9, 9, 6, 1, 26.00),
        (10, 10, 10, 1, 38.00);
    """))

print("✅ Dados inseridos com sucesso no banco loja_bolos!")
