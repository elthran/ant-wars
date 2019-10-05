<template>
  <div id="app">
    <hello-world />
  </div>
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
