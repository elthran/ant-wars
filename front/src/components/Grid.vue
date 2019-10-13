<template lang="pug">
  v-layer#grid
    v-rect(:config="configBackground")
    //- v-line
</template>

<script>
export default {
  name: 'Grid',
  components: {
  },
  props: {
    width: Number,
    height: Number,
  },
  data () {
    return {
      configBackground: {
        x: 0,
        y: 0,
        width: this.width,
        height: this.height,
        fill: 'black',
      }
    }
  },
  computed: {},
  mounted () {
    // console.log('this.width', this.width)
    // console.log('this.height', this.height)
  },
  methods: {},
}
</script>

<style lang='sass' scoped>
// .grid
//   background: black
//   width: 100vh
//   height: 100vh
</style>
