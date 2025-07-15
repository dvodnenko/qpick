function Header() {
    return (
        <header>
            <div class="headerItem">
                <div class="logo">
                    <h2 style={{cursor: "pointer"}}>QPICK</h2>
                </div>
            </div>

            <div class="headerItem">
                <div class="heartGroup">
                    <span title="liked products" style={{cursor: "pointer"}}>❤️</span>
                </div>
                <div class="cartGroup">
                    <span title="your cart" style={{cursor: "pointer"}}>🛒</span>
                </div>
            </div>
        </header>
    )
}

export default Header
