import { Link } from "react-router-dom"

function Header({titleContent}) {
    return (
        <header>
            <div className="headerItem">
                <div className="logo">
                    <Link to='/' >
                        <h2 style={{cursor: "pointer"}}>{titleContent}</h2>
                    </Link>
                </div>
            </div>

            <div className="headerItem">
                <div className="cartGroup">
                    <Link to='/mycart' >🛒</Link>
                </div>
            </div>
        </header>
    )
}

export default Header
