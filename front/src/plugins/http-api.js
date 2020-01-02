import axios from 'axios'

// customize config here.
const instance = axios.create({
  baseURL: '/api/', // ?? or maybe something else if dev mode?
  // timeout: 1000,
  // headers: {'X-Custom-Header': 'foobar'}
});

export default instance
