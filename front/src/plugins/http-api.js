import axios from 'axios'

function baseUrl () {
  if (process.env.NODE_ENV === 'development') {
    return 'http://localhost:5000/api'
  } else {
    return '/api'
  }
}

// customize config here.
const customAxios = axios.create({
  baseURL: baseUrl(),
  timeout: 1000,
})

// var xhttp = new XMLHttpRequest();
// xhttp.onreadystatechange = function () {
//   if (this.readyState == 4 && this.status == 200) {
//     console.log(this.responseText)
//   }
// }
// xhttp.open("GET", "grow", true);
// xhttp.send();

export default customAxios
