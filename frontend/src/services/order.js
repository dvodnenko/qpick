import API from "../utils/api"
import { getSessionKey } from "../utils/session"


export const orderMyCart = async () => {
    const sessionKey = getSessionKey()
    console.log(sessionKey)

    const data = {
        session_key: sessionKey,
    }

    let response = await API.post('/api/order', data)
    console.log(response.data)
    return response.data
}
