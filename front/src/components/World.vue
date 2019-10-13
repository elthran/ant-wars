<template lang="pug">
  v-stage#world(:config="configKonva")
      v-layer
        v-circle(:config="configCircle")
</template>

<script>
export default {
  name: 'World',
  data () {
    return {
      configKonva: {
        width: 200,
        height: 200,
      },
      configCircle: {
        x: 100,
        y: 100,
        radius: 70,
        fill: "red",
        stroke: "black",
        strokeWidth: 4,
      },
    }
  },
}
</script>
