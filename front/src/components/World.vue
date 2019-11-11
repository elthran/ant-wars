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
    )
    leaves
</template>

<script>
import Ants from './Ants'
import Grid from './Grid'
import Leaves from './Leaves'

export default {
  name: 'World',
  components: {
    Grid,
    Ants,
    Leaves,
  },
  props: {
  },
  data () {
    return {
      gridSpacing: 25,
      ants: this.randomAnts()
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
    // layer.draw()
    // console.log('this.width', this.width)
  },
  methods: {
    randomBetween(min = 3, max = 20) {
      return Math.floor((Math.random() * (max-min)) + min) // 1-100
    },
    roundToMultiple(value, interval) {
      const diffInterval = value % interval
      if (diffInterval < interval / 2.0) {
        return value - diffInterval
      } else {
        return value + (interval - diffInterval)
      }
    },
    randomAnts() {
      let ants = []
      let numOfAnts = this.randomBetween(2, 20)

      do {
        ants.push({
          id: numOfAnts,
          x: this.randomXCoord(),
          y: this.randomYCoord(),
        })
        numOfAnts--
      } while (numOfAnts > 0)

      return ants
    },
    randomXCoord() {
      return this.randomBetween(1, this.xGridUnits) * 25
    },
    randomYCoord() {
      return this.randomBetween(1, this.yGridUnits) * 25
    },
  }
}
</script>

<style lang='sass' scoped>
</style>

