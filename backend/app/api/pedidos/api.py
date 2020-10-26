from flask import jsonify, request
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
from app.models.pedido import Pedido
from app.database.pedidos import PedidosSchema

pedido_schema = PedidosSchema()
pedidos_schema = PedidosSchema(many=True)

class PedidosResource(Resource):
    # @http_auth_required
    def get(self):

        pedido = Pedido()
        result = pedido.get_pedidos()

        return pedidos_schema.dump(result)

    def post(self):
        json_input = request.get_json()
        errors = pedido_schema.validate(json_input)
        if errors:
            return {
                    'error': errors
                }

        pedido = Pedido()
        pedido.set_data_pedido(json_input['data_pedido'])
        pedido.set_status_pedido(json_input['status_pedido'])
        pedido.set_valor_pedido(json_input['valor_pedido'])
        pedido.set_cliente_id(json_input['cliente_id'])
        result = pedido.save()
        return result, 201

class PedidoResource(Resource):

    def get(self, id):
        pedido = Pedido()
        pedido.set_id(id)
        if not pedido.get_pedido_json():
            return {
                "error": "Pedido não encontrado"
            }
        result = pedido.get_pedido()
        # print(result)
        return pedido_schema.dump(result)
        

    def delete(self, id):
        pedido = Pedido()
        pedido.set_id(id)
        if not pedido.get_pedido_json():
            return {
                "error": "Pedido não encontrado"
            }
        ped = pedido.delete()
        return pedido_schema.dump(ped)

    def put(self, id):
        json_input = request.get_json()
        
        pedido = Pedido()
        pedido.set_id(id)

        if not pedido.get_pedido_json():
            return {
                "error": "Pedido não encontrado"
            }
        errors = pedido_schema.validate(json_input)
        if errors:
            return {
                "error": errors
            }

        pedido.set_data_pedido(json_input['data_pedido'])
        pedido.set_status_pedido(json_input['status_pedido'])
        pedido.set_valor_pedido(json_input['valor_pedido'])
        pedido.set_cliente_id(json_input['cliente_id'])
        result = pedido.update()
        return result, 201

