import { useEffect, useState } from "react"
import API from "../utils/api"

import Header from "./Header"
import Banner from "./Banner"
import HeadphoneCard from "./HeadphoneCard"
import CoverCard from "./CoverCard"
import Footer from "./Footer"

import { getCart } from "../services/cart"


function Home() {
    const [loading, setLoading] = useState(true)

    const [headphones, setHeadphones] = useState([])
    const [covers, setCovers] = useState([])

    const [cart, setCart] = useState(null)


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

        async function fetchCart() {
            let cart = await getCart()
            setCart(cart)
        }
        
        fetchData()
        fetchCart()
        
    }, [])

    if (loading) return <div>Loading...</div>;

    return (
        <>
            <Header titleContent={'QPICK'} />

            <Banner />

            <main>
                {headphones.length > 0 ? <h3>Headphones</h3> : <h3>No Headphones Found</h3>}
                <section>
                    {headphones.map((element, index) => (
                        <HeadphoneCard product={element} key={`headphone-card-${index}`} includeButton={true} />
                    ))}
                </section>

                {covers.length > 0 ? <h3>Covers</h3> : <h3>No Covers Found</h3>}
                <section>
                    {covers.map((element, index) => (
                        <CoverCard product={element} key={`cover-card-${index}`} includeButton={true} />
                    ))}
                </section>
            </main>

            <Footer />
        </>
    )
}

export default Home
