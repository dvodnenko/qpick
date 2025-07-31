import API from '../utils/api'
import { getSessionKey } from '../utils/session'


export const addToCartRequest = async (productId, productType, quantity = 1) => {
    const sessionKey = getSessionKey()

    const data = {
        product_id: productId,
        product_type: productType,
        quantity: quantity,
        session_key: sessionKey,
    }
    
    try {
        await API.post('/api/cart/add/', data)
    }
    catch (error) {
        let errorText = error.response.data.error
        alert(errorText)
    }
}

export const getCart = async () => {
    const sessionKey = getSessionKey()

    let response = await API.get(`/api/cart?session_key=${sessionKey}`)

    return response.data
}
