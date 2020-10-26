from flask import Blueprint
from flask_restful import Api
from flask_security import login_required

from app.api.clientes.api import ClientesResource, ClienteResource
from app.api.pedidos.api import PedidosResource, PedidoResource

bp_api = Blueprint("api", __name__, url_prefix="/")

api = Api(bp_api)

def init_app(app):
    api.add_resource(ClientesResource, "clientes")
    api.add_resource(ClienteResource, 'clientes/<id>')
    api.add_resource(PedidosResource, "pedidos")
    api.add_resource(PedidoResource, 'pedidos/<id>')
    
    app.register_blueprint(bp_api)
