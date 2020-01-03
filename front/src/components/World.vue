<template lang="pug">
  v-stage#world(:config="configKonva")
    grid(
      :width="width"
      :height="height"
      :line-width="1"
      :gridSpacing="gridSpacing"
    )
    ants(
      :ants="ants"
      :gridSpacing="gridSpacing"
    )
    foods(
      :foods="foods"
    )
</template>

<script>
import Ants from './Ants'
import Grid from './Grid'
import Foods from './Foods'
import growApi from '@/api/grow-api'

export default {
  name: 'World',
  components: {
    Grid,
    Ants,
    Foods,
  },
  props: {
  },
  data () {
    return {
      gridSpacing: 25,
      // ants: this.randomAnts(),
      // leaves: this.randomLeaves(),
      ants: [],
      foods: [],
    }
  },
  computed: {
    width () { return window.innerWidth },
    height () { return window.innerHeight },
    xGridUnits () { return this.width / this.gridSpacing },
    yGridUnits () { return this.height / this.gridSpacing },
    configKonva () {
      return {
        width: this.width,
        height: this.height,
      }
    },
  },
  mounted () {
    console.log('this.xGridUnits', this.xGridUnits)
    console.log('this.yGridUnits', this.yGridUnits)
    // layer.draw()
    // console.log('this.width', this.width)
    growApi.grow()
      .then((world) => {
        console.log('world', world)
        console.log('world.colonies[0]', world.colonies[0])
        console.log('world.colonies[0].ants', world.colonies[0].ants)
        console.log('world.foods', world.foods)
        this.ants = world.colonies[0].ants
        this.foods = world.foods

      })
    // this.interval =  setInterval(() => {
    //   this.world = growApi.grow()
    //   console.log('Growing!!!')
    // }, 5000);
  },
  beforeDestroy () {
    // clearInterval(this.interval);
  },
}
</script>

<style lang='sass' scoped>
</style>

