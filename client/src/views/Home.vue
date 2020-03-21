<template>
  <div class="home" id="map">
    <UsaMap />
  </div>
</template>

<script>
// @ is an alias to /src
import UsaMap from '@/components/UsaMap.vue';

export default {
  name: 'Home',
  components: {
    UsaMap,
  },
};
</script>
