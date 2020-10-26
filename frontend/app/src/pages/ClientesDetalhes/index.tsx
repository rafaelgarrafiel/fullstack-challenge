import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Nav from '../../components/Nav'
import Sidenav from '../../components/Sidenav'

import api from '../../service/api'

interface ClienteParams {
    id: string;
}

interface Cliente {
    id: number;
    primeiro_nome: string;
    ultimo_nome: string;
    email: string;
}

const ClientesDetalhes:React.FC = () => {

    const [cliente, setCliente] = useState<Cliente>();

    const { id } = useParams<ClienteParams>();

    useEffect(() => {
        async function getItems() {
            try {
                const { data } = await api.get(`/clientes/${id}`);
                setCliente(data);
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
                            {cliente && (
                                <div className="col-md-8 order-md-1">
                                    <h4 className="mb-3">Informações do Cliente</h4>
                                    <div className="row">
                                        <div className="col-md-6 mb-3">
                                            <label>Primeiro Nome</label>
                                            <input type="text" className="form-control" value={cliente.primeiro_nome}/>
                                        </div>
                                        <div className="col-md-6 mb-3">
                                            <label>Ultimo Nome</label>
                                            <input type="text" className="form-control" value={cliente.ultimo_nome}/>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="col-md-12 mb-3">
                                            <label>Email</label>
                                            <input type="text" className="form-control" value={cliente.email}/>
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

export default ClientesDetalhes;
