import { addToCartRequest } from "../services/cart"


function CoverCard({product, includeButton = false}) {

    if (includeButton) {
        return (
            <div className="card cover-card" >
                <div class="cardHeartContainer">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.09.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>
                    </svg>
                </div>
                <img src={product.image} alt="/src/assets/default-image.webp" className="earPodsImage" />
                <div className="cardInfo">
                    <div className="left">
                        <div className="cardName">{product.title}</div>
                        <div className="cardPrice">{product.price}</div>
                    </div>
                    <div className="right">
                        <div className="max-quantity">Units in Stock: {product.quantity}</div>
                    </div>
                </div>
                <button onClick={() => {
                        let quantity = prompt('Enter Quantity: ')
        
                        if (quantity <= 0) {
                            alert('Error: Quantity Must be Greater Than 0')
                            return null
                        }
        
                        addToCartRequest(product.id, 'Cover', quantity)
                    }}>Add To Cart</button>
            </div>
        )
    } else {
        return (
            <div className="card cover-card" >
                <div class="cardHeartContainer">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.09.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>
                    </svg>
                </div>
                <img src={product.image} alt="/src/assets/default-image.webp" className="earPodsImage" />
                <div className="cardInfo">
                    <div className="cardName">{product.title}</div>
                    <div className="cardPrice">{product.price}</div>
                </div>
            </div>
        )
    }
}

export default CoverCard
