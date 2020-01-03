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
    gridSpacing: {
      type: Number,
      default () {
        return 25
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
      const foodConfig = {
        ...this.foodBaseConfig,
        ...food,
        src: `/assets/images/${food.type || 'leaf'}.jpg`,
      }
      const foodWithLocalCoords = this.mapToLocalCoordinateSystem(foodConfig)
      return foodWithLocalCoords
    },
    mapToLocalCoordinateSystem (food) {
      food.x *= this.gridSpacing
      food.y *= this.gridSpacing
      return food
    },
  },
}
</script>

<style lang='sass' scoped>
</style>
