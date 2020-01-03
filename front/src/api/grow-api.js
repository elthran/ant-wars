// This should only be used during developtment
// The backend should grow on its own.

import http from '@/plugins/http-api';

export default {
  create () {},
  read () {},
  update () {},
  delete () {},
  grow () {
    return http.get('/grow')
      .then(response => {
        return response.data.world
      })
      .catch(error => {
        console.log(error.toJSON())
        // debugger
      })
  }
}
