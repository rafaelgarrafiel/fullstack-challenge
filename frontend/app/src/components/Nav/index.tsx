import React from 'react';
import { Link } from 'react-router-dom';

const Nav:React.FC = () => {
    return (
        <nav className="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
            <Link className="navbar-brand col-md-3 col-lg-2 mr-0 px-3" to='/'>
                Sistema
            </Link>
            <button className="navbar-toggler position-absolute d-md-none collapsed" type="button" data-toggle="collapse" data-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <ul className="navbar-nav px-3">
                <li className="nav-item text-nowrap">
                    <Link className="navbar-brand col-md-3 col-lg-2 mr-0 px-3" to='/'>
                        Usuário
                    </Link>
                </li>
            </ul>
        </nav>
    )
}

export default Nav;