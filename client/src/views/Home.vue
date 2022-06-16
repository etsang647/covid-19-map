<template>
  <div class="home">
    <div v-if="isLoaded">
      <h1 class>COVID-19 in the United States</h1>
      <Forms :dataType="dataType" :dates="dates"
        @input-changed="updateInputs" @error-changed="updateError" />
      <Map :mapInfo="mapInfo" :dataType="dataType" :mapData="mapData" />
      <p>
        created by Eric Tsang |
        <a href="https://github.com/etsang647/covid-19-map">github</a>
      </p>
    </div>
    <h1 v-else>Loading...</h1>
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
      mapData: {
        startData: {},
        endData: {},
      },
      mapInfo: {
        error: false,
        msg: 'Hover over a state for more details',
      },
    };
  },
  mounted() {
    this.setUpApp();
  },
  methods: {
    // fetch NYT dataset from server
    async fetchData() {
      const path = 'http://localhost:5000/data'; // local Flask server
      // const path = '/data'; // production server
      let response;
      try {
        response = await fetch(path);
      } catch (error) {
        console.error(error);
      }
      return response.json();
    },
    // by default, set startDate and endDate to the 2 most recent dates in dataset
    // also set date boundaries for date input
    setDefaultDates() {
      const datasetArr = Object.keys(this.dataset);
      [this.dates.min] = datasetArr;
      this.dates.max = datasetArr[datasetArr.length - 1];
      this.dates.start = datasetArr[datasetArr.length - 2];
      this.dates.end = this.dates.max;
    },
    updateMapData() {
      const startDate = this.dates.start;
      const endDate = this.dates.end;
      this.mapData.startData = this.dataset[startDate];
      this.mapData.endData = this.dataset[endDate];
    },
    async setUpApp() {
      try {
        this.dataset = await this.fetchData();
      } catch (error) {
        console.error(error);
        alert('Failed to fetch data');
        return;
      }
      this.dataType = 'cases';
      this.setDefaultDates();
      this.updateMapData();
      this.isLoaded = true;
    },
    updateInputs(newInputs) {
      this.dataType = newInputs.dataType;
      this.dates.start = newInputs.startDate;
      this.dates.end = newInputs.endDate;
      this.updateMapData();
      this.mapInfo.msg = 'Hover over a state for more details';
      this.mapInfo.error = false;
    },
    updateError(errorMsg) {
      this.mapInfo.error = true;
      this.mapInfo.msg = errorMsg;
    },
  },
};
</script>
