function Footer() {
    return (
        <footer>
            <div className="footerItem">
                <div className="logo">Qpick</div>
            </div>

            <div className="footerItem">
                <nav>
                    <li><a href="">Вибране</a></li>
                    <li><a href="">кошик</a></li>
                    <li><a href="">Контакти</a></li>
                </nav>
            </div>

            <div className="footerItem languagesBox">
                <div className="footerItem_top">
                    <span>Умови сервісу</span>
                </div>
                <div className="footerItem_bottom">
                    <img src="img/earth.png" alt="" />
                    <span>Esp </span>
                    <span style={{color: '#ffa542', fontWeight: 700}}>Укр </span>
                    <span>Eng</span>
                </div>
            </div>
            <div className="social">
                <img src="src/assets/Instagram.png" alt="" />
                <img src="src/assets/Telegram.png" alt="" />
                <img src="src/assets/Whatsapp.png" alt="" />
            </div>
        </footer>
    )
}

export default Footer
