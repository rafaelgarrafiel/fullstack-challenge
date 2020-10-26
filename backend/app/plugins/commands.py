from app.plugins.database import db
from app.database.clientes import Clientes
from app.database.pedidos import Pedidos


def create_db():
    """Criando o banco de dados"""
    db.create_all()


def drop_db():
    """Limpando o banco de dados"""
    db.drop_all()


def populate_db():
    """Populando o banco de dados"""
    data = [
        Clientes(primeiro_nome='Cliente', ultimo_nome='1', email='cliente1@email.com'),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()

    data_pedido = [
        Pedidos(data_pedido='22-10-2020', status_pedido='Encaminhado', valor_pedido='22.00', cliente_id=1),
    ]
    db.session.bulk_save_objects(data_pedido)
    db.session.commit()
    return True