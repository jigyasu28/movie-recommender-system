import "./list.scss"
import ArrowBackIos from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIos from '@mui/icons-material/ArrowForwardIos';
import Listitem from "../listitem/Listitem";
import { useEffect, useRef, useState } from "react";
import axios from "axios";
import { axiosInstance } from "../../config";
export default function List({genre,setCurrent}) {

  const [genreMovie,setGenreMovie] = useState([])
  
  useEffect(()=>{
        const getGenre = async () =>{
        try{
           console.log("check");
            const res = await axiosInstance.post("/getGenreMovie/", {genre: genre})

            setGenreMovie(res.data);
            console.log(genreMovie)
        }catch(err){
            console.log(err);
        }
    }
    getGenre()
  },[])




  const [slideNumber,setSlideNumber] = useState(0)
  const listRef = useRef()

  const handleClick = (direction) =>{
      let distance = listRef.current.getBoundingClientRect().x - 50
      if(direction === "left" && slideNumber>0){
          setSlideNumber(slideNumber-1)
         listRef.current.style.transform = `translateX(${400 + distance}px)`
      }

      if(direction === "right" && slideNumber<4){
          setSlideNumber(slideNumber+1)
         listRef.current.style.transform = `translateX(${-400 + distance}px)`
      }
  }

  return (
    <div className='list'>
     <span className="listtitle">{genre}</span>
     <div className="wrapper">
       <ArrowBackIos className="sliderArrow left" onClick={()=>handleClick("left")}/>
        <div className="container" ref = {listRef} >
          { genreMovie.map (
                (element) =>(
                       <div className="suggestions" onClick={()=>{
                          // setCurrent(element)
                          console.log(element.movie_id)
                          // setArr([])
                       }}>
                           <Listitem id={element.movie_id} setCurrent={setCurrent}/>
                      </div>
                )
            )}
        </div>
       <ArrowForwardIos className="sliderArrow right" onClick={()=>handleClick("right")}/>
     </div>
    </div>
  )
}
