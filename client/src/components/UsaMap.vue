<template>
  <svg-map :map="USA" :location-class="getLocationClass" @click="exampleReq()" />
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
      amount: '',
    };
  },
  methods: {
    getAmount(payload) {
      const path = 'http://localhost:5000/';
      axios
        .post(path, payload)
        .then((res) => {
          this.amount = res.data.amount;
          console.log('amount is', this.amount);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    exampleReq() {
      const payload = {
        name: 'New York',
        date: '3/19/20',
      };
      this.getAmount(payload);
    },
    getLocationClass(location, index) {
      console.log(location, index);
      if (location.name === 'Wyoming') {
        return 'svg-map__location color';
      }
      return '';
    },
  },
};
</script>

<style>
.color {
  fill: gold;
}
.color:hover {
  opacity: 0.75;
}
</style>
