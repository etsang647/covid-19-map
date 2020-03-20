<template>
  <svg-map :map="USA" @click="getAmount()" />
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
      date: '3/19/20',
      amount: '',
    };
  },
  methods: {
    getAmount() {
      const path = 'http://localhost:5000/';
      axios
        .get(path)
        .then((res) => {
          this.amount = res.data.amount;
          console.log('amount is', this.amount);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>

<style src="vue-svg-map/dist/index.css"></style>
