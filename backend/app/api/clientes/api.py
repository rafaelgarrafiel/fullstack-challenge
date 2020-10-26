from flask import jsonify, request, abort
from flask_restful import Resource, reqparse
from flask_security import auth_token_required, http_auth_required
from marshmallow import (
    Schema,
    fields,
    validate,
    pre_load,
    post_dump,
    post_load,
    ValidationError,
)

from app.models.cliente import Cliente
from app.database.clientes import ClientesSchema

cliente_schema = ClientesSchema()
clientes_schema = ClientesSchema(many=True)

class ClientesResource(Resource):
    def get(self):
        
        cliente = Cliente()
        result = cliente.get_clientes()

        return clientes_schema.dump(result)

    def post(self):
        json_input = request.get_json()
        errors = cliente_schema.validate(json_input)
        if errors:
            return {
                    'error': errors
                }
        cliente = Cliente()
        cliente.set_primeiro_nome(json_input['primeiro_nome'])
        cliente.set_ultimo_nome(json_input['ultimo_nome'])
        cliente.set_email(json_input['email'])
        result = cliente.save()

        return result, 201


class ClienteResource(Resource):

    def get(self, id):
        cliente = Cliente()
        cliente.set_id(id)
        if not cliente.get_cliente_json():
            return {
                "error": "Cliente não encontrado"
            }
        result = cliente.get_cliente()

        return cliente_schema.dump(result)

    def delete(self, id):
        cliente = Cliente()
        cliente.set_id(id)

        if not cliente.get_cliente_json():
            return {
                "error": "Cliente não encontrado"
            }
        
        cli = cliente.delete()
        return  cliente_schema.dump(cli)

    def put(self, id):
        json_input = request.get_json()
        cliente = Cliente()
        cliente.set_id(id)

        if not cliente.get_cliente_json():
            return {
                "error": "Cliente não encontrado"
            }
        errors = cliente_schema.validate(json_input)
        if errors:
            return {
                "error": errors
            }
        
        cliente.set_primeiro_nome(json_input['primeiro_nome'])
        cliente.set_ultimo_nome(json_input['ultimo_nome'])
        cliente.set_email(json_input['email'])
        result = cliente.update()
        return result, 201
