from sqlalchemy import text
from app.plugins.database import db
from app.database.pedidos import Pedidos, PedidosSchema
from app.database.clientes import Clientes

pedido_schema = PedidosSchema()
pedidos_schema = PedidosSchema(many=True)

class Pedido():

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_data_pedido(self):
        return self.__data_pedido

    def set_data_pedido(self, data_pedido):
        self.__data_pedido = data_pedido
    
    def get_status_pedido(self):
        return self.__status_pedido

    def set_status_pedido(self, status_pedido):
        self.__status_pedido = status_pedido
    
    def get_valor_pedido(self):
        return self.__valor_pedido

    def set_valor_pedido(self, valor_pedido):
        self.__valor_pedido = valor_pedido
    
    def get_cliente_id(self):
        return self.__cliente_id

    def set_cliente_id(self, cliente_id):
        self.__cliente_id = cliente_id
    
    def get_pedido_json(self):
        pedido = Pedidos.query.filter(Pedidos.id==self.get_id()).filter(Pedidos.ativo == True).first()
        return pedido_schema.dump(pedido)
    
    def save(self):
        try:
            pedido = Pedidos()
            pedido.data_pedido = self.get_data_pedido()
            pedido.status_pedido = self.get_status_pedido()
            pedido.valor_pedido = self.get_valor_pedido()
            pedido.cliente_id = self.get_cliente_id()
            db.session.add(pedido)
            db.session.flush()
        except Exception as e:
            db.session.rollback()
            raise e
        
        db.session.commit()

        return pedido_schema.dump(pedido)
    
    def update(self):
        try:
            pedido = Pedidos.query.filter(Pedidos.id==self.get_id()).first()
            pedido.data_pedido = self.get_data_pedido()
            pedido.status_pedido = self.get_status_pedido()
            pedido.valor_pedido = self.get_valor_pedido()
            pedido.cliente_id = self.get_cliente_id()
            db.session.flush()
        except Exception as e:
            db.session.rollback()
            raise e
        
        db.session.commit()

        return pedido_schema.dump(pedido)
    
    def delete(self):
        try:
            pedido = Pedidos.query.filter(Pedidos.id==self.get_id()).first()
            pedido.ativo = False
            db.session.flush()
        except Exception as e:
            db.session.rollback()
            raise e
        
        db.session.commit()

        return pedido_schema.dump(pedido)

    def get_pedidos(self):
        registros = Pedidos.query.filter(
            Pedidos.ativo == True
            ).outerjoin(Clientes,
                (Pedidos.cliente_id == Clientes.id)
                )\
            .values(
                    Pedidos.id,
                    Pedidos.data_pedido,
                    Pedidos.valor_pedido,
                    Pedidos.status_pedido,
                    Clientes.primeiro_nome.label('cliente')
                    )

        return registros
    
    def get_pedido(self):
        registros = Pedidos.query.filter(
            Pedidos.ativo == True,
            Pedidos.id == self.get_id()
            ).outerjoin(Clientes,
                (Pedidos.cliente_id == Clientes.id)
                )\
            .values(
                    Pedidos.id,
                    Pedidos.data_pedido,
                    Pedidos.valor_pedido,
                    Pedidos.status_pedido,
                    Clientes.primeiro_nome.label('cliente')
                    )

        return registros