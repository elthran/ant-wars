<template lang="pug">
  div
    h1 Hello World
</template>

<script>
export default {
  name: 'Leaves',
  components: {
  },
  props: {

  },
  data () {
    return {}
  },
  computed: {},
  methods: {},
  v-layer
    v-group(
      v-for="leaf in leaves"
      :key="leaf.id"
    )
      k-image(:config="buildLeafConfig(leaf)")
</template>

<script>
import KImage from './KImage'

export default {
  name: 'Leaves',
  components: {
    KImage,
  },
  props: {
    leaves: {
      type: Array,
      default () {
        return []
      },
    },
  },
  data () {
    return {
      leafBaseConfig: {
        x: 0,
        y: 0,
        type: 'leaf',
        src: '/assets/images/leaf.jpg',
      },
    }
  },
  computed: {},
  methods: {
    buildLeafConfig (leaf) {
      return {
        ...this.leafBaseConfig,
        ...leaf,
        src: `/assets/images/${leaf.type || 'leaf'}.jpg`,
      }
    }
  },
}
</script>

<style lang='sass' scoped>
</style>
