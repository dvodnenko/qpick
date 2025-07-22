export const getSessionKey = () => {
    let sessionKey = localStorage.getItem('session_key')
    if (!sessionKey) {
        sessionKey = crypto.randomUUID()
        localStorage.setItem('session_key', sessionKey)
    }
    return sessionKey
}
