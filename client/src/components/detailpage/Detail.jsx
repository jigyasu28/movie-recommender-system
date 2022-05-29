import React, { useEffect, useState } from 'react'
import axios from "axios"
import RecommendationCard from '../RecommendationCard/RecommendationCard'
import "./details.scss"
import { axiosInstance } from '../../config'

export default function Detail({id, setCurrent}) {
   function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
  const [recommend,setRecommend] = useState([])
  useEffect(()=>{
      const getRecommendation = async()=>{
         try{
           const recommended = await axiosInstance.post("/getRecommendation/", {id : id})
           setRecommend(recommended.data)
           console.log(recommended.data,id)
           
         }catch(err){
           console.log(err);
         }
      }
      getRecommendation()
  },[id])
 
  const forwardSlash = "//"
  const [budget,setBudget] = useState(null)
  const [revenue,setRevenue] = useState(null)
  const [movie,setMovie] = useState(null)
  useEffect(()=>{
    const getMovie = async ()=>{
             try{
         const res = await axios.get("https://api.themoviedb.org/3/movie/"+id+"?api_key=03f4b7c839caf675aaecbbf85e86257a&language=en-US")
        setMovie(res.data) 
        const number = numberWithCommas(res.data.revenue)
        
        if (number=="0"){
          setRevenue("Unknown")
        }
        else{
          setRevenue(number)
        }
        const number2 = numberWithCommas(res.data.budget)
        
        if (number=="0"){
          setBudget("Unknown")
        }
        else{
          setBudget(number2)
        }
        console.log(res.data)   
       }catch(err){
          console.log(err)
     }
    }
   getMovie()
  },[id])
  return (
    // <div><h1>{movie?.title}</h1></div>
      <div className='detail'>
      <div className="flex-container">

        <div className="flex-child magenta">
             <img className="posterImage" src={"https://image.tmdb.org/t/p/w500/"+movie?.poster_path}/>
         </div>
  
       <div className="details">
             {movie?.title}
             <br/>
             <br/>
             {movie?.overview}
             <br/>
             <br/>
             Release Date: {movie?.release_date}
             <br/>
             Duration: {movie?.runtime} Minutes
             <br/>
             <br/>
             Budget: {budget} USD
             <br/>
             Revenue: {revenue} USD
             <br/>
             <br/>
             Imdb Link: <a href={"https://www.imdb.com/title/"+movie?.imdb_id}>https:{forwardSlash}www.imdb.com/title/{movie?.imdb_id}</a>
             <br/>
             Watch Here: <a href={movie?.homepage}>{movie?.homepage}</a>
       </div>
        
  
      </div>
       <div className='similarMovies'>Similar movies like {movie?.title} </div>
      {recommend.map((element)=>(
      <RecommendationCard id={element.movie_id} setCurrent={setCurrent}/>
      ))}
       
      </div>
  )
}

