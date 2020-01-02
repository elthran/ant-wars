<template lang='pug'>
  #app
    world
</template>

<script>
import World from '@/components/World'

export default {
  name: 'App',
  components: {
    World
  },
  data () {
    return {
    }
  },
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
