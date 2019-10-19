<template lang="pug">
  v-layer#grid
    v-rect(:config="configBackground")
    v-group#horizontal-lines(
      v-for="offset in horizontalLines"
      :key="offset.id"
    )
      v-line(:config="buildHorizontalConfigLine(offset)")
    v-group#vertical-lines(
      v-for="offset in verticalLines"
      :key="offset.id"
    )
      v-line(:config="buildVerticalConfigLine(offset)")
</template>

<script>
import { cloneDeep } from 'lodash'

export default {
  name: 'Grid',
  components: {},
  props: {
    background: {
      type: String,
      default: '#262626', // off-black
    },
    height: {
      type: Number,
      required: true,
    },
    lineColour: {
     type: String,
      default: '#f2f2f2', // off-white
    },
    gridSpacing: {
      type: Number,
      default: 50,
    },
    lineWidth: {
      type: Number,
      default: 3,
    },
    width: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      configBackground: {
        x: 0,
        y: 0,
        width: this.width,
        height: this.height,
        fill: this.background,
      },
      configLineBase: {
        points: [0, 0, 0, 0],
        stroke: this.lineColour,
        strokeWidth: this.lineWidth,
      },
    }
  },
  computed: {
    horizontalLines() {
      return this.buildLineOffsets(this.height)
    },
    verticalLines() {
      return this.buildLineOffsets(this.width)
    },
  },
  mounted() {},
  methods: {
    buildLineOffsets(maximum) {
      let lineOffsets = []
      let line = 1
      let offset

      do {
        offset = line * this.gridSpacing
        lineOffsets.push(offset)
        line++
      } while (offset < maximum)
      return lineOffsets
    },
    buildHorizontalConfigLine(offset) {
      let config = cloneDeep(this.configLineBase)
      config.points[1] = offset
      config.points[2] = this.width
      config.points[3] = offset

      return config
    },
    buildVerticalConfigLine(offset) {
      let config = cloneDeep(this.configLineBase)
      config.points[0] = offset
      config.points[2] = offset
      config.points[3] = this.height

      return config
    },
  },
}
</script>

<style lang="sass" scoped>
// .grid
//   background: black
//   width: 100vh
//   height: 100vh
</style>
