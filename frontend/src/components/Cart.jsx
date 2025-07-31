import Header from "./Header"
import Footer from "./Footer"
import HeadphoneCard from "./HeadphoneCard"
import CoverCard from "./CoverCard"
import { orderMyCart } from "../services/order"


function Cart({cartItems}) {
    let totalPriceUSD = 0
    let totalPriceUAH = 0

    cartItems.map((cartItem, _) => {
        if (cartItem.product.currency === '$') {
            totalPriceUSD += cartItem.product.price * cartItem.quantity
        } else if (cartItem.product.currency === '₴') {
            totalPriceUAH += cartItem.product.price * cartItem.quantity
        }
    })

    let totalPriceString = ''
    if (totalPriceUAH == 0 && totalPriceUSD == 0)       totalPriceString = '0'
    else if (totalPriceUSD > 0 && totalPriceUAH == 0)   totalPriceString = `$${totalPriceUSD}`
    else if (totalPriceUSD == 0 && totalPriceUAH > 0)   totalPriceString = `₴${totalPriceUAH}`
    else if (totalPriceUAH > 0 && totalPriceUSD > 0)    totalPriceString = `$${totalPriceUSD} + ₴${totalPriceUAH}`

    return (
        <>
            <Header titleContent={'My Cart'} />

            <main>
                <div className="cart-info">
                    <div className="buy-button-container">
                        <button onClick={() => {
                            orderMyCart()
                        }}>Order Everything in Cart</button>
                    </div>

                    <span style={{
                        fontWeight: 800,
                        fontSize: '17px'
                    }}>Total Price: {totalPriceString}</span>
                </div>

                {cartItems.length > 0 ? <h3>My Cart Items</h3> : <h3>No Items in Your Cart yet</h3>}
                <section>
                    {cartItems.map((element, index) => {
                        if (element.product_type === 'Headphone') {
                            return <HeadphoneCard product={element.product} key={`headphone-card-${index}`} includeButton={false} />
                        } else if (element.product_type === 'Cover') {
                            return <CoverCard product={element.product} key={`cover-card-${index}`} includeButton={false}  />
                        }
                    }
                    )}
                </section>
            </main>

            <Footer />
        </>
    )
}


export default Cart
