from flask import jsonify
from sqlalchemy import text
from app.plugins.database import db
from app.database.clientes import Clientes, ClientesSchema

cliente_schema = ClientesSchema()
clientes_schema = ClientesSchema(many=True)

class Cliente():
    
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_primeiro_nome(self):
        return self.__primeiro_nome

    def set_primeiro_nome(self, primeiro_nome):
        self.__primeiro_nome = primeiro_nome
    
    def get_ultimo_nome(self):
        return self.__ultimo_nome

    def set_ultimo_nome(self, ultimo_nome):
        self.__ultimo_nome = ultimo_nome
    
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
    
    def get_cliente_json(self):
        cliente = Clientes.query.filter(Clientes.id==self.get_id()).filter(Clientes.ativo == True).first()
        return cliente_schema.dump(cliente)
    
    def save(self):
        
        try:
            cliente = Clientes()
            cliente.primeiro_nome = self.get_primeiro_nome()
            cliente.ultimo_nome = self.get_ultimo_nome()
            cliente.email = self.get_email()
            db.session.add(cliente)
            db.session.flush()
        except Exception as e:
            db.session.rollback()
            return False
        
        db.session.commit()

        return cliente_schema.dump(cliente)
    
    def update(self):
        
        try:
            cliente = Clientes.query.filter(Clientes.id==self.get_id()).first()
            cliente.primeiro_nome = self.get_primeiro_nome()
            cliente.ultimo_nome = self.get_ultimo_nome()
            cliente.email = self.get_email()
            db.session.flush()
        except Exception as e:
            db.session.rollback()
            raise e
        
        db.session.commit()

        return cliente_schema.dump(cliente)
    
    def delete(self):
        try:
            cliente = Clientes.query.filter(Clientes.id==self.get_id()).first()
            cliente.ativo = False
            db.session.flush()
        except Exception as e:
            db.session.rollback()
            return False
        
        db.session.commit()

        return cliente_schema.dump(cliente)
    
    def get_clientes(self):
        return Clientes.query.filter(Clientes.ativo == True).all()
    
    def get_cliente(self):
        return Clientes.query.filter(Clientes.id==self.get_id()).filter(Clientes.ativo == True).first()