<template lang='pug'>
  #app
    hello-world
</template>

<script>
import HelloWorld from '@/components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data () {
    return {
    }
  },
}
</script>

<style type="text/scss">
.hello-world {
  color: red;
}
</style>
