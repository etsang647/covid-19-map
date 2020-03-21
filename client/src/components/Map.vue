<template>
  <States :classes="classes" />
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
      cases: {},
      classes: {},
    };
  },
  created() {
    this.getCases({ date: '03-20-2020' });
  },
  methods: {
    getCases(date) {
      const path = 'http://localhost:5000/';
      axios
        .post(path, date)
        .then((res) => {
          this.cases = res.data.cases;
          this.classes = res.data.classes;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
