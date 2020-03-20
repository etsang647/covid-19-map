<template>
  <svg-map :map="USA" />
</template>

<script>
import { SvgMap } from 'vue-svg-map';
import USA from '@svg-maps/usa';

export default {
  name: 'UsaMap',
  components: {
    SvgMap,
  },
  data() {
    return {
      USA,
    };
  },
};
</script>

<style src="vue-svg-map/dist/index.css"></style>
