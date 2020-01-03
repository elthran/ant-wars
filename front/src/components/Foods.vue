<template lang="pug">
  v-layer
    v-group(
      v-for="food in foods"
      :key="food.id"
    )
      k-image(:config="buildFoodConfig(food)")
</template>

<script>
import KImage from './KImage'

export default {
  name: 'Foods',
  components: {
    KImage,
  },
  props: {
    foods: {
      type: Array,
      default () {
        return []
      },
    },
  },
  data () {
    return {
      foodBaseConfig: {
        x: 0,
        y: 0,
        type: 'food',
        src: '/assets/images/leaf.jpg',
      },
    }
  },
  computed: {},
  methods: {
    buildFoodConfig (food) {
      return {
        ...this.foodBaseConfig,
        ...food,
        src: `/assets/images/${food.type || 'leaf'}.jpg`,
      }
    },
  },
}
</script>

<style lang='sass' scoped>
</style>
