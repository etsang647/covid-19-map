<template>
  <div>
    <p>{{ details }}</p>
    <States :dates="dates" :response="response" :date="date" :type="type"
    @hover-state="showDetails" @unhover-state="hideDetails"
    @valid-date="validDate" />
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
      details: 'Loading...',
      valid: false,
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
      this.validDate(this.valid);
    },
    validDate(val) {
      if (val) {
        this.updateDetails('Hover over a state for more details');
        this.valid = true;
      } else {
        const endDate = new Date();
        endDate.setDate(endDate.getDate() - 1); // yesterday

        const formattedDate = endDate.toLocaleString('en-US', {
          month: '2-digit',
          day: '2-digit',
          year: 'numeric',
        });

        this.valid = false;

        const invalidStr = `Error: Invalid date or date outside range (01/21/2020 - ${formattedDate})`;
        this.updateDetails(invalidStr);
      }
    },
    updateDetails(str) {
      this.details = str;
    },
  },
};
</script>
