import Navbar from "../components/navbar/navbar.jsx"
import "./home.scss"
import List from "../components/list/List.jsx"
import { useState } from "react"
import Detail from "../components/detailpage/Detail.jsx"

const Home = () => {
  const [genreList, setGenreList] = useState(["Action", "Comedy","Romance","Adventure","ScienceFiction","Fantasy","Crime","Thriller","Drama","Documentary"])
  const [currentMovie,setCurrent] = useState(null)
  return (
    <div className='home'>
     <Navbar setCurrent={setCurrent}/>
    {/*  <img width = "100%" src= {logo} 
           alt=""
  /> */}
  <div className="content-container">
  {
    currentMovie==null?
    
    <div>
        {genreList.map(
          (element) =>(
            <List genre={element} setCurrent={setCurrent}/>
          )
        )}
    </div>
    :<Detail id = {currentMovie.movie_id} setCurrent={setCurrent}/>
       
  }
  </div>

    </div>
  )
}

export default Home