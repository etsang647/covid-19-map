<template>
  <div class="home">
    <h1 class="header">{{ headerText }}</h1>
    <div v-if="isLoaded">
      <Forms :dataType="dataType" :defaultDates="dates"
        @valid-input="updateInputs" @invalid-input="updateError" />
      <Map :dataType="dataType" :mapData="mapData" :mapError="mapError" />
      <p class="footer">
        created by Eric Tsang |
        <a href="https://github.com/etsang647/covid-19-map">github</a>
      </p>
    </div>
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
      dataType: 'cases',
      dates: {
        start: '',
        end: '',
        min: '',
        max: '',
      },
      mapData: {
        startData: {},
        endData: {},
      },
      mapError: {
        error: false,
        msg: 'Hover over a state for more details',
      },
    };
  },
  mounted() {
    this.setUpApp();
  },
  computed: {
    headerText() {
      return this.isLoaded ? 'COVID-19 in the United States' : 'Loading...';
    },
  },
  methods: {
    setDefaultDates() {
      const datasetArr = Object.keys(this.dataset);
      // eslint-disable-next-line prefer-destructuring
      this.dates.min = datasetArr[0];
      this.dates.max = datasetArr[datasetArr.length - 1];
      // by default, start and end are the 2 most recent dates in the dataset
      this.dates.start = datasetArr[datasetArr.length - 2];
      this.dates.end = this.dates.max;
    },
    updateMapData() {
      const startDate = this.dates.start;
      const endDate = this.dates.end;
      this.mapData.startData = this.dataset[startDate];
      this.mapData.endData = this.dataset[endDate];
    },
    // handler for valid form inputs
    updateInputs(newInputs) {
      this.dataType = newInputs.dataType;
      this.dates.start = newInputs.startDate;
      this.dates.end = newInputs.endDate;
      this.updateMapData();

      this.mapError.error = false;
      this.mapError.msg = 'Hover over a state for more details';
    },
    // handler for invalid form inputs
    updateError(errorMsg) {
      this.mapError.error = true;
      this.mapError.msg = errorMsg;
    },
    // fetch NYT dataset from server
    async fetchData() {
      // const path = 'http://localhost:5000/data'; // local Flask server
      const path = '/data'; // production server
      let response;
      try {
        response = await fetch(path);
      } catch (error) {
        console.error(error);
      }
      return response.json();
    },
    async setUpApp() {
      try {
        this.dataset = await this.fetchData();
      } catch (error) {
        console.error(error);
        alert('Failed to fetch data');
        return;
      }
      this.setDefaultDates();
      this.updateMapData();
      this.isLoaded = true;
    },
  },
};
</script>
