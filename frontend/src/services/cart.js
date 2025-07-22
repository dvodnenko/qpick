import API from '../utils/api'
import { getSessionKey } from '../utils/session'


export const addToCart = async (productId, quantity = 1) => {
    const sessionKey = getSessionKey()
    return API.post('/api/cart/add/', {
        session_key: sessionKey,
        product_id: productId,
        quantity,
    })
}

export const getCart = async () => {
  const sessionKey = getSessionKey()
  await API.get('/api/cart', { params: { session_key: sessionKey } })
    .then((response) => {return response.data})
}
