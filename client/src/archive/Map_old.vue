<template>
  <div>
    <p>{{ details }}</p>
    <States :response="response" :start="start" :date="date" :type="type"
    @hover-state="showDetails" @unhover-state="hideDetails"
    @valid-date="validDate" />
  </div>
</template>

<script>
// import axios from 'axios';
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
      details: '',
      valid: false,
    };
  },
  props: ['start', 'date', 'type', 'dateCheck'],
  created() {
    // this.getCases();
  },
  methods: {
    getCases() {
      const path = 'http://localhost:5000/data'; // local Flask server
      // const path = '/data'; // production server
      // axios
      //   .get(path)
      //   .then((res) => {
      //     this.dates = res.data.dates;
      //     this.response = true;
      //     this.getEndDate();
      //   })
      //   .catch((error) => {
      //     // eslint-disable-next-line
      //     console.error(error);
      //   });
      fetch(path)
        .then((res) => res.json())
        .then((data) => {
          this.dates = data.dates;
          this.response = true;
          this.getEndDate();
        });
    },
    getEndDate() {
      const datesArray = Object.keys(this.dates);
      const endDate = datesArray[datesArray.length - 1];
      const startDate = datesArray[datesArray.length - 2];

      this.$emit('start-date', startDate);
      this.$emit('end-date', endDate);
      this.$emit('loaded');
      return endDate;
    },
    showDetails(str) {
      this.details = str;
    },
    hideDetails() {
      this.validDate(this.valid);
    },
    // shows helpful message if val is true, otherwise shows error message
    validDate(val) {
      if (val) {
        if (this.dateCheck) {
          this.updateDetails('Hover over a state for more details');
        } else {
          this.updateDetails('Warning: Start date is later than end date');
        }
        this.valid = true;
      } else {
        const endDate = new Date(this.getEndDate());

        // format endDate into mm/dd/yyyy format
        const formattedDate = endDate.toLocaleString('en-US', {
          month: '2-digit',
          day: '2-digit',
          year: 'numeric',
        });

        const invalidStr = `Error: Invalid date, or date outside range (01/21/2020 - ${formattedDate})`;
        this.updateDetails(invalidStr);
        this.valid = false;
      }
    },
    updateDetails(str) {
      this.details = str;
    },
  },
};
</script>
