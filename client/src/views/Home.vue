<template>
  <div class="home" v-if="isLoaded">
    <h1 class="header">COVID-19 in the United States</h1>
    <Forms :dataType="dataType" :dates="dates" @input-changed="updateInputs"
      @date-out-of-bounds="outOfBoundsError" @date-out-of-order="outOfOrderError" />
    <Map :dataType="dataType" :dates="dates" :info="info"
      :startData="getStartData()" :endData="getEndData()" />
    <p>
      created by Eric Tsang |
      <a href="https://github.com/etsang647/covid-19-map">github</a>
    </p>
  </div>
</template>

<script>
import Map from '../components/Map.vue';
import Forms from '../components/Forms.vue';

export default {
  components: { Map, Forms },
  name: 'Home',
  data() {
    return {
      isLoaded: false,
      dataset: {},
      dataType: '',
      dates: {
        start: '',
        end: '',
        min: '',
        max: '',
      },
      info: {
        msg: 'Hover over a state for more details',
        error: false,
      },
    };
  },
  mounted() {
    this.setUpApp();
  },
  computed: {
    headerText() {
      const startDate = this.formatDate(this.dates.start);
      const endDate = this.formatDate(this.dates.end);
      return `COVID-19 ${this.dataType} from ${startDate} to ${endDate}`;
    },
  },
  methods: {
    // fetch NYT dataset from server
    async fetchData() {
      const path = 'http://localhost:5000/data'; // local Flask server
      // const path = '/data'; // production server
      const response = await fetch(path);
      return response.json();
      // catch here???
    },
    // by default, set startDate and endDate to the 2 most recent dates in dataset
    // also set date boundaries for date input
    setDefaultDates() {
      const datasetArr = Object.keys(this.dataset);
      this.dates.start = datasetArr[datasetArr.length - 2];
      this.dates.end = datasetArr[datasetArr.length - 1];
      // eslint-disable-next-line prefer-destructuring
      this.dates.min = datasetArr[0];
      this.dates.max = this.dates.end;
    },
    getStartData() {
      return this.dataset[this.dates.start];
    },
    getEndData() {
      return this.dataset[this.dates.end];
    },
    async setUpApp() {
      const data = await this.fetchData();
      this.dataset = data.dates;
      // catch this too
      this.dataType = 'cases';
      this.setDefaultDates();
      this.isLoaded = true;
    },
    updateInputs(newInputs) {
      this.dataType = newInputs.dataType;
      this.dates.start = newInputs.startDate;
      this.dates.end = newInputs.endDate;
      this.info.msg = 'Hover over a state for more details';
      this.info.error = false;
    },
    // format date string from yyyy-mm-dd to mm/dd/yyyy
    formatDate(date) {
      const [year, month, day] = date.split('-');
      const newDate = [month, day, year].join('/');
      return newDate;
    },
    outOfBoundsError() {
      const minDate = this.formatDate(this.dates.min);
      const maxDate = this.formatDate(this.dates.max);
      this.info.msg = `Date must be in range [${minDate}, ${maxDate}]`;
      this.info.error = true;
    },
    outOfOrderError() {
      this.info.msg = 'Start date must come before end date';
      this.info.error = true;
    },
  },
};
</script>
