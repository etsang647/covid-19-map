<template>
  <div>
    <p>{{ details }}</p>
    <States :dates="dates" :response="response" :date="date" :type="type"
    @hover-state="showDetails" @unhover-state="hideDetails"/>
  </div>
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
      details: 'Hover over a state for more details',
    };
  },
  props: ['date', 'type'],
  created() {
    this.getCases();
  },
  methods: {
    getCases() {
      const path = 'http://localhost:5000/data'; // local Flask server
      // const path = '/data'; // production server
      axios
        .get(path)
        .then((res) => {
          this.dates = res.data.dates;
          this.response = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    showDetails(str) {
      this.details = str;
    },
    hideDetails() {
      this.details = 'Hover over a state for more details';
    },
  },
};
</script>
