import React from 'react';
import { Link } from 'react-router-dom';

const Sidenav:React.FC = () => {
    return (
        <nav id="sidebarMenu" className="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
            <div className="sidebar-sticky pt-3">
                <ul className="nav flex-column">
                    <li className="nav-item">
                        <Link
                            className="nav-link active"
                            to={`/`}
                        >
                            <span data-feather="home"></span>
                            Principal <span className="sr-only">(current)</span>
                        </Link>
                        <Link
                            className="nav-link active"
                            to={`/clientes`}
                        >
                            <span data-feather="home"></span>
                            Clientes <span className="sr-only"></span>
                        </Link>
                        <Link
                            className="nav-link active"
                            to={`/pedidos`}
                        >
                            <span data-feather="home"></span>
                            Pedidos <span className="sr-only"></span>
                        </Link>
                    </li>
                </ul>
            </div>
        </nav>
    )
}

export default Sidenav;