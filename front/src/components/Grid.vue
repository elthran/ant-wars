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
    width: Number,
    height: Number,
  },
  data() {
    return {
      configBackground: {
        x: 0,
        y: 0,
        width: this.width,
        height: this.height,
        fill: '#262626',
      },
      lineOffset: 25,
      configLine: {
        points: [0, 0, 0, 0],
        stroke: '#f2f2f2',
        strokeWidth: 3,
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
        offset = line * this.lineOffset
        lineOffsets.push(offset)
        line++
      } while (offset < maximum)
      return lineOffsets
    },
    buildHorizontalConfigLine(offset) {
      let config = cloneDeep(this.configLine)
      config.points[1] = offset
      config.points[2] = this.width
      config.points[3] = offset

      return config
    },
    buildVerticalConfigLine(offset) {
      let config = cloneDeep(this.configLine)
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
