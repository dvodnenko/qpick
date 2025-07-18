import { useEffect, useState } from "react"
import API from "../api"

import Header from "./Header"


function Home() {
    const [loading, setLoading] = useState(true)

    const [headphones, setHeadphones] = useState([])
    const [covers, setCovers] = useState([])


    useEffect(() => {
        async function fetchData() {
            await API.get('/api/headphones')
            .then((response) => {
                setHeadphones(response.data);
            })
            .catch((error) => {
                console.log('this error occurred while fetching "headphones": ', error)
                return null
            })

            await API.get('/api/covers')
            .then((response) => {
                setCovers(response.data);
            })
            .catch((error) => {
                console.log('this error occurred while fetching "covers": ', error)
                return null
            })

            setLoading(false);
            return null
        }

        fetchData()
    }, [])

    if (loading) return <div>Loading...</div>;

    return (
        <>
            <Header />
        </>
    )
}

export default Home
