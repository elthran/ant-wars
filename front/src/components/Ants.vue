<template lang="pug">
  v-layer
    v-group(
      v-for="ant in ants"
      :key="ant.id"
    )
      k-image(:config="buildAntConfig(ant)")
</template>

<script>
import KImage from './KImage'

export default {
  name: 'Ants',
  components: {
    KImage
  },
  props: {
    ants: {
      type: Array,
      default () {
        return []
      },
    },
  },
  data () {
    return {
      antBaseConfig: {
        x: 0,
        y: 0,
        type: 'ant',
        src: '/assets/images/ant.jpg',
      },
    }
  },
  computed: {},
  mounted () {
  },
  methods: {
    buildAntConfig (ant) {
      return {
        ...this.antBaseConfig,
        ...ant,
        src: `/assets/images/${ant.type || 'ant'}.jpg`,
      }
    }
  },
}
</script>

<style lang='sass' scoped>
</style>
