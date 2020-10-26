import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";

import Nav from '../../components/Nav'
import Sidenav from '../../components/Sidenav'

import api from '../../service/api'

interface Cliente {
    id: number;
    primeiro_nome: string;
    ultimo_nome: string;
    email: string;
}

const Clientes:React.FC = () => {

    const [clientes, setClientes] = useState([]);

    useEffect(() => {
        async function getItems() {
            try {
                const { data } = await api.get("/clientes");
                setClientes(data);
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

                        <h2>Clientes</h2>
                        <div className="table-responsive">
                            <table className="table"> 
                                <thead>
                                    <tr>
                                        <th>Primeiro Nome</th>
                                        <th>Ultimo Nome</th>
                                        <th>Email</th>
                                        <th>Ações</th>
                                    </tr>
                                </thead>
                                <tbody>
                                {clientes.map((cliente: Cliente) => (
                                    <tr key={cliente.id}>
                                        <td>{cliente.primeiro_nome}</td>
                                        <td>{cliente.ultimo_nome}</td>
                                        <td>{cliente.email}</td>
                                        <td>
                                            <Link
                                                to={`/clientes/${cliente.id}`}
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

export default Clientes;
