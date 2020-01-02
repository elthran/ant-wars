import axios from 'axios'

// function baseUrl () {
//   if (process.env.NODE_ENV === 'development') {
//     return 'http://localhost:5000/api'
//   } else {
//     return '/api'
//   }
// }

// customize config here.
const customAxios = axios.create({
  // baseURL: baseUrl(),
  // baseURL: baseUrl(),
  // timeout: 1000,
})

export default customAxios
