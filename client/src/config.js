import axios from "axios";

export const axiosInstance = axios.create({
	baseURL : "https://http://127.0.0.1:5000/"
})
