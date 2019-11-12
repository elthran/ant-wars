<template lang="pug">
  v-image(:config="imageConfig")
</template>

<script>
export default {
  name: 'KImage',
  props: {
    config: {
      type: Object,
    },
  },
  data() {
    return {
      imageConfig: {
        image: null,
      }
    }
  },
  computed: {
  },
  mounted () {
    Object.assign(this.imageConfig, this.config)

    const image = new window.Image()
    image.src = this.config.src

    image.onload = () => {
      // set image only when it is loaded
      this.imageConfig.image = image
    }
  },
}
</script>
