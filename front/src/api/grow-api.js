// This should only be used during developtment
// The backend should grow on its own.

import http from '@/plugins/http-api';

export default {
  create () {},
  read () {},
  update () {},
  delete () {},
  grow () {
    console.log('runing grow')
    return http.get('/grow')
      .then(response => {
        console.log(response.data);
        console.log(response.status);
        console.log(response.statusText);
        console.log(response.headers);
        console.log(response.config);
      })
      .catch(error => {
        console.log(error.toJSON())
        // debugger
      })
  }
}
