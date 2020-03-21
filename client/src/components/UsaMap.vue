<template>
  <svg-map :map="USA" :location-class="getLocationClass" />
</template>

<script>
import { SvgMap } from 'vue-svg-map';
import USA from '@svg-maps/usa';
import axios from 'axios';

export default {
  name: 'UsaMap',
  components: {
    SvgMap,
  },
  data() {
    return {
      USA,
      cases: {},
      class: '',
    };
  },
  methods: {
    getAmount(payload) {
      const path = 'http://localhost:5000/';
      axios
        .post(path, payload)
        .then((res) => {
          this.cases[payload.name] = res.data.amount;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getLocationClass(location) {
      this.getAmount({ name: location.name, date: '3/19/20' });
      if (parseFloat(this.cases[location.name]) > 100) {
        return 'color-1';
      }
      return 'color-2';
    },
  },
  created() {
    this.getAmount({ name: 'New York', date: '3/19/20' });
  },
};
</script>
