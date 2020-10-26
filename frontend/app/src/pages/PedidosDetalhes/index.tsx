import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Nav from '../../components/Nav'
import Sidenav from '../../components/Sidenav'

import api from '../../service/api'

interface PedidoParams {
    id: string;
}

interface Pedido {
    id: number;
    cliente: string;
    data_pedido: string;
    valor_pedido: string;
    status_pedido: string;
}

const PedidosDetalhes:React.FC = () => {

    const [pedido, setPedido] = useState<Pedido>();

    const { id } = useParams<PedidoParams>();

    useEffect(() => {
        async function getItems() {
            try {
                const { data } = await api.get(`/pedidos/${id}`);
                setPedido(data);
            } catch (error) {
                alert("Ocorreu um erro ao buscar os items");
            }
        }
        getItems();
    }, [id])

    return (
        <>
            <Nav />
            <div className="container-fluid">
                <div className="row">

                    <Sidenav />
                    <main role="main" className="col-md-9 ml-sm-auto col-lg-10 px-md-4">

                        <h2>Clientes</h2>
                        <div className="table-responsive">
                            {pedido && (
                                <div className="col-md-8 order-md-1">
                                    <h4 className="mb-3">Informações do Pedido</h4>
                                    <div className="row">
                                        <div className="col-md-6 mb-3">
                                            <label>Cliente</label>
                                            <input type="text" className="form-control" value={pedido.cliente}/>
                                        </div>
                                        <div className="col-md-6 mb-3">
                                            <label>Data do Pedido</label>
                                            <input type="text" className="form-control" value={pedido.data_pedido}/>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="col-md-6 mb-3">
                                            <label>Valor do Pedido</label>
                                            <input type="text" className="form-control" value={pedido.valor_pedido}/>
                                        </div>
                                        <div className="col-md-6 mb-3">
                                            <label>Status do Pedido</label>
                                            <input type="text" className="form-control" value={pedido.status_pedido}/>
                                        </div>
                                    </div>
                                </div>
                            )}
                        </div>
                    </main>
                </div>
            </div>
        </>
    );
};

export default PedidosDetalhes;
