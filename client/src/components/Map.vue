<template>
  <States :dates="dates" :response="response" />
</template>

<script>
import axios from 'axios';
import States from '@/components/States.vue';

export default {
  name: 'Map',
  components: {
    States,
  },
  data() {
    return {
      dates: {},
      response: false,
    };
  },
  created() {
    this.getCases();
  },
  methods: {
    getCases() {
      const path = '/data';
      axios
        .post(path)
        .then((res) => {
          this.dates = res.data.dates;
          this.response = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
