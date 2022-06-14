<template>
  <div class="home">
    <h1 class="header">{{ headerText }}</h1>
    <!-- wrap these forms up in a component later -->
    <form action="" class="date-and-type">
      <label for="type">Type:</label>
      <select name="" id="" v-model="dataType">
        <option value="cases">cases</option>
        <option value="deaths">deaths</option>
      </select>

      <label for="date">Start date:</label>
      <input type="date" class="date-picker" v-model="startDate" :min="minDate" :max="maxDate">

      <label for="date">End date:</label>
      <input type="date" class="date-picker" v-model="endDate" :min="minDate" :max="maxDate">
    </form>
    <Map v-if="isLoaded" :dataType="dataType"
    :startData="getStartData()" :endData="getEndData()" />
  </div>
</template>

<script>
import Map from '../components/Map.vue';

export default {
  components: { Map },
  name: 'Home',
  data() {
    return {
      isLoaded: false,
      dataset: {},
      dataType: 'cases',
      startDate: '',
      endDate: '',
      minDate: '',
      maxDate: '',
    };
  },
  mounted() {
    this.setUpApp();
  },
  computed: {
    headerText() {
      const str = `COVID-19 ${this.dataType} from ${this.startDate} to ${this.endDate}`;
      return str;
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
      this.startDate = datasetArr[datasetArr.length - 2];
      this.endDate = datasetArr[datasetArr.length - 1];
      // eslint-disable-next-line prefer-destructuring
      this.minDate = datasetArr[0];
      this.maxDate = this.endDate;
    },
    getStartData() {
      return this.dataset[this.startDate];
    },
    getEndData() {
      return this.dataset[this.endDate];
    },
    async setUpApp() {
      const data = await this.fetchData();
      this.dataset = data.dates;
      // catch this too
      this.setDefaultDates();
      this.isLoaded = true;
    },
  },
};
</script>
