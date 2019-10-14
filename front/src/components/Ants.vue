<template lang="pug">
  v-layer
    k-image(:config="imageConfig")
</template>

<script>
import KImage from './KImage'

export default {
  name: 'Ants',
  components: {
    KImage
  },
  props: {

  },
  data () {
    return {
      imageConfig: {
        x: 200,
        y: 50,
        src: '/assets/images/ant.jpg',
      },
    }
  },
  computed: {},
  mounted () {
  },
  methods: {},
}
</script>

<style lang='sass' scoped>
</style>
