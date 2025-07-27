import Header from "./Header"
import Banner from "./Banner"
import HeadphoneCard from "./HeadphoneCard"
import CoverCard from "./CoverCard"
import Footer from "./Footer"
import '../App.css'


function Home({headphones, covers}) {

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
