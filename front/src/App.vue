<template>
  <div id="app">
    {{ message }}
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      message: 'Hello World!'
    }
  }
}
</script>

<style type="text/scss">
.hello-world {
  color: red;
}
</style>
