<template>
  <div class="home">
    <h1 class="header">Showing {{ type }} as of {{ date }}</h1>
    <Map id="map" :date="date" :type="type" />
  </div>
</template>

<script>
// @ is an alias to /src
import Map from '@/components/Map.vue';

export default {
  name: 'Home',
  components: {
    Map,
  },
  data() {
    return {
      date: '2020-03-30',
      type: 'cases',
    };
  },
};
</script>
