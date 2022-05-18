<template>
  <div class="home">
    <h1 class="header">COVID-19 {{ type }} from {{ formatDate(start) }} to
      {{ formatDate(date) }}</h1>
    <form class="date-and-type">
      <label for="date">Start date:</label>
      <input type="date" class="date-picker" v-model="start"
      min="2020-01-21" :max="endDate" >

      <label for="date">End date:</label>
      <input type="date" class="date-picker" v-model="date"
      min="2020-01-21" :max="endDate" >

      <label for="type">Type:</label>
      <select v-model="type">
        <option value="cases">cases</option>
        <option value="deaths">deaths</option>
      </select>
    </form>
    <Map id="map" :start="start" :date="date" :type="type" @end-date="getEndDate" />
  </div>
</template>

<script>
// @ is an alias to /src
import Map from '@/components/Map.vue';

export default {
  name: 'Home',
  components: {
    Map,
  },
  data() {
    return {
      start: '',
      date: '',
      type: 'cases',
      endDate: '', // for date input upper bound
    };
  },
  methods: {
    // format date from yyyy-mm-dd to mm/dd/yyyy
    formatDate(date) {
      const selectedDate = new Date(date);
      selectedDate.setUTCHours(0, 0, 0, 0); // convert from local time to UTC midnight

      const formattedDate = selectedDate.toLocaleString('en-US', {
        month: '2-digit',
        day: '2-digit',
        year: 'numeric',
        timeZone: 'UTC',
      });

      return formattedDate;
    },
    // gets end date of dataset (i.e. yesterday's date)
    getEndDate(endDate) {
      this.start = '2020-01-21';
      this.date = endDate;
      this.endDate = endDate;
    },
  },
};
</script>
