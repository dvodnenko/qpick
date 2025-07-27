function Header({titleContent}) {
    return (
        <header>
            <div className="headerItem">
                <div className="logo">
                    <h2 style={{cursor: "pointer"}}>{titleContent}</h2>
                </div>
            </div>

            <div className="headerItem">
                <div className="heartGroup">
                    <span title="liked products" style={{cursor: "pointer"}}>❤️</span>
                </div>
                <div className="cartGroup">
                    <span title="your cart" style={{cursor: "pointer"}}>🛒</span>
                </div>
            </div>
        </header>
    )
}

export default Header
