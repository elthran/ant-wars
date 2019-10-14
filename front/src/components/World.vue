<template lang="pug">
  v-stage#world(:config="configKonva")
    grid(
      :width="width"
      :height="height"
    )
    ants
</template>

<script>
import Grid from './Grid'
import Ants from './Ants'

export default {
  name: 'World',
  components: {
    Grid,
    Ants,
  },
  data () {
    return {
    }
  },
  computed: {
    width () { return window.innerWidth },
    height () { return window.innerHeight },
    configKonva () {
      return {
        width: this.width,
        height: this.height,
      }
    },
  },
  mounted () {
    // layer.draw()
    // console.log('this.width', this.width)
  }
}
</script>

<style lang='sass' scoped>
</style>

