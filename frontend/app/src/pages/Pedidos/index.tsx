import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";

import Nav from '../../components/Nav'
import Sidenav from '../../components/Sidenav'

import api from '../../service/api'

interface Pedido {
    id: number;
    cliente: string;
    data_pedido: string;
    valor_pedido: string;
    status_pedido: string;
}

const Pedidos:React.FC = () => {

    const [pedidos, setPedidos] = useState([]);

    useEffect(() => {
        async function getItems() {
            try {
                const { data } = await api.get("/pedidos");
                setPedidos(data);
            } catch (error) {
                alert("Ocorreu um erro ao buscar os items");
            }
        }
        getItems();
    }, [])

    return (
        <>
            <Nav />
            <div className="container-fluid">
                <div className="row">

                    <Sidenav />
                    <main role="main" className="col-md-9 ml-sm-auto col-lg-10 px-md-4">

                        <h2>Pedidos</h2>
                        <div className="table-responsive">
                            <table className="table"> 
                                <thead>
                                    <tr>
                                        <th>Cliente</th>
                                        <th>Data da Compra</th>
                                        <th>Valor da Compra</th>
                                        <th>Ações</th>
                                    </tr>
                                </thead>
                                <tbody>
                                {pedidos.map((pedido: Pedido) => (
                                    <tr key={pedido.id}>
                                        <td>{pedido.cliente}</td>
                                        <td>{pedido.data_pedido}</td>
                                        <td>{pedido.valor_pedido}</td>
                                        <td>
                                            <Link
                                                to={`/pedidos/${pedido.id}`}
                                            >
                                                Detalhar
                                            </Link>
                                        </td>
                                    </tr>
                                ))}
                                </tbody>
                            </table>
                        </div>
                    </main>
                </div>
            </div>
        </>
    );
};

export default Pedidos;
