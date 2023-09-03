import axios from "axios"

const request = axios.create({
    baseURL: '/api',
    timeout: 3 * 1000
})
export default request
