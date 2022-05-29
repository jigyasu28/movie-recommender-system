import "./navbar.scss";
import HomeIcon from '@mui/icons-material/Home';
import logo from './logo.png'
import ArrowDropDown from '@mui/icons-material/ArrowDropDown';
import { useRef, useState } from "react";
import axios from "axios"
import { axiosInstance } from "../../config";
const Navbar = ({setCurrent}) => {
       const inputRef = useRef()
       const [showSuggestions,setShowSuggestions] = useState(false)
       const [arr, setArr] = useState([]);
       const [selection,setSelection] = useState(0)
    const handleChange = async (e) =>{

        try{
           console.log("check");
            const res = await axiosInstance.post("/search/", {
                value: e.target.value,
                selection: selection
            })

            setArr(res.data);
                   if (e.target.value===""){
          setShowSuggestions(false)
       }
       else{
          setShowSuggestions(true)
       }
            console.log(arr)
        }catch(err){
            console.log(err);
        }
    }
  return (
     <>
    <div className="navbar">
         <div className="container">
     {/*   <div className="center">
        <h3>  <img src= {logo} 
           alt="My Movie Reccomendor"
               /> 
  JigyasuFlix </h3>  </div> */}
           <div className="center2" >
           <span className="title-logo" onClick={()=>{
              setCurrent(null)
           }}>JigyasuFlix</span>
        <span  onClick={()=>{
              setCurrent(null)
           }}> Home</span>
          {/* <span>SearchBy
           <select name="searchby" id="searchby" >
              <option onClick={()=>{
                 setSelection(0)
              }} value="1">Movies</option>
              <option onClick={()=>{
                 setSelection(1)
              }} value="2">Genres</option>
           </select>
           </span> 8/}
           
            {/* <span className="options">Movies</span>
             <span className="options">Genres</span>
             <span className="options">Genres</span>
             <span className="options">check</span>
  </span>*/}
         <input className="search" type="text" placeholder="Search here..." onChange={handleChange} ref={inputRef}></input> 
     
            </div>
         </div>  
    </div>
    <div className="suggestion-container">
    {
                showSuggestions && arr.map(
                (element) =>(
                       <div className="suggestion" onClick={()=>{
                          setCurrent(element)
                          console.log(element.movie_id)
                          setArr([])
                          inputRef.current.value = "";
                       }}>
                           <div className="movieOption">
                           
                              {element.title}
                           
                           </div>
                      </div>
                )
            )
                     }
                     </div>
                     </>
  )
}

export default Navbar