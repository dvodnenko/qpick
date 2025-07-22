import API from '../utils/api'
import { getSessionKey } from '../utils/session'


export const addToCart = async (productId, quantity = 1) => {
    const sessionKey = getSessionKey()

    const data = {
        product_id: productId,
        quantity: quantity,
        session_key: sessionKey,
    }
    
    await API.post('/api/cart/add/', data)
}
