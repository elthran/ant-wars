<template lang='pug'>
  #app
    world
</template>

<script>
import World from '@/components/World'
import growApi from '@/api/grow-api'

export default {
  name: 'App',
  components: {
    World
  },
  data () {
    return {
    }
  },
  mounted () {
    growApi.grow()
  }
}
</script>

<style lang="sass">
// global styles
body
  box-sizing: border-box
  margin: 0
  padding: 0
  overflow: hidden
</style>
