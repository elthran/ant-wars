<template lang="pug">
  v-stage#world(:config="configKonva")
    grid(
      :width="width"
      :height="height"
    )
    v-layer
      v-circle(:config="configCircle")
</template>

<script>
import Grid from './Grid'

export default {
  name: 'World',
  components: {
    Grid
  },
  data () {
    return {
      configCircle: {
        x: 100,
        y: 100,
        radius: 70,
        fill: "red",
        stroke: "black",
        strokeWidth: 4,
      },
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

