import React from 'react';
import { Switch, Route } from "react-router-dom";

import Dashboard from '../pages/Dashboard';
import Clientes from '../pages/Clientes';
import ClientesDetalhes from '../pages/ClientesDetalhes';
import Pedidos from '../pages/Pedidos';
import PedidosDetalhes from '../pages/PedidosDetalhes';

const Routes:React.FC = () => (
    <Switch>
        <Route path="/" component={Dashboard} exact />
        <Route path="/clientes" component={Clientes} exact />
        <Route path="/clientes/:id" component={ClientesDetalhes} />
        <Route path="/pedidos" component={Pedidos} exact />
        <Route path="/pedidos/:id" component={PedidosDetalhes} />
    </Switch>
);

export default Routes;
