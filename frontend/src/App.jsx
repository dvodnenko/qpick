import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'

import API from './utils/api'
import Home from './components/Home'
import Cart from './components/Cart'
import { getCart } from './services/cart'


function App() {
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

  if (loading) return <div>Loading...</div>

  return (
    <>
    <div className='wrap'>
      <Router>
        <Routes>
          <Route path='/' element={<Home headphones={headphones} covers={covers} />} />
          <Route path='/mycart' element={<Cart cartItems={cart} />} />
        </Routes>
      </Router>
    </div>
    </>
  )
}

export default App
