import API from "../utils/api"
import { getSessionKey } from "../utils/session"


export const orderMyCart = async () => {
    const sessionKey = getSessionKey()

    const data = {
        session_key: sessionKey,
    }

    let response = null

    try {
        response = await API.post('/api/order', data)
    }
    catch (error) {
        let errorText = error.response.data.error
        alert(errorText)
        return
    }

    console.log(response.data)
    return response.data
}
