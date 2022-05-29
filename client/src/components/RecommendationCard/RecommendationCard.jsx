
import React, { useEffect, useState } from 'react'
import axios from "axios"
export default function RecommendationCard({id,setCurrent}) {
   const [movie,setMovie] = useState(null)
  useEffect(()=>{
        const getMovie = async ()=>{
             try{
        const res = await axios.get("https://api.themoviedb.org/3/movie/"+id+"?api_key=03f4b7c839caf675aaecbbf85e86257a&language=en-US")
          setMovie(res.data)
        // console.log(movie)   
       }catch(err){
          console.log(err)
     }
    }
    getMovie()
  },[id])

  return (
    <div className="recommendations" onClick={()=>{
 
      setCurrent({
        ...movie,movie_id:movie.id
      });
      console.log(movie.id)
    }}>
     <img src={"https://image.tmdb.org/t/p/w500/"+movie?.poster_path}/>
    </div>
  )
}
