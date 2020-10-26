from marshmallow import (
    Schema,
    fields,
    validate,
    pre_load,
    post_dump,
    post_load,
    validates_schema,
    ValidationError,
)

from app.plugins.database import db
from app.database.clientes import Clientes

class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_pedido = db.Column(db.String(255))
    status_pedido = db.Column(db.String(255))
    valor_pedido = db.Column(db.String(255))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    clientes = db.relationship('Clientes', backref=db.backref('pedidos', lazy=True))
    ativo = db.Column(db.Boolean(), default=True)

class PedidosSchema(Schema):
    id = fields.Int()
    data_pedido = fields.Str(required=True, error_messages={
        "required": "Informe o primeiro nome",
        "null": "Campo não pode ser vazio"
    })
    status_pedido = fields.Str(
        required=True, 
        error_messages={
            "required": "Informe o ultimo nome",
            "null": "Campo não pode ser vazio"
        }
    )
    valor_pedido = fields.Str(
        required=True, 
        error_messages={
            "required": "Informe o ultimo nome",
            "null": "Campo não pode ser vazio"
        }
    )
    cliente = fields.Str()
    cliente_id = fields.Int(
        required=True, 
        error_messages={
            "required": "Informe o ultimo nome",
            "null": "Campo não pode ser vazio"
        }
    )