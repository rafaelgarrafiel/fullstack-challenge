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

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(255))
    ultimo_nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    ativo = db.Column(db.Boolean(), default=True)

class ClientesSchema(Schema):
    id = fields.Int()
    primeiro_nome = fields.Str(required=True, error_messages={
        "required": "Informe o primeiro nome",
        "null": "Campo não pode ser vazio"
    })
    ultimo_nome = fields.Str(
        required=True, 
        error_messages={
            "required": "Informe o ultimo nome",
            "null": "Campo não pode ser vazio"
        }
    )
    email = fields.Str(
        required=True, 
        error_messages={
            "required": "Informe um email",
            "null": "Campo não pode ser vazio"
        },
        validate=validate.Email(error="Digite um email válido")
    )
