<template>
  <div class="home">
    <h1 class="header">Cumulative COVID-19 {{ type }} as of {{ formatDate(date) }}</h1>
    <form class="date-and-type">
      <label for="date">Date:</label>
      <input type="date" id="date-picker" v-model="date"
      min="2020-01-21" :max="endDate" >

      <label for="type">Type:</label>
      <select v-model="type">
        <option value="cases">cases</option>
        <option value="deaths">deaths</option>
      </select>
    </form>
    <Map id="map" :date="date" :type="type" @end-date="getEndDate" />
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
      this.date = endDate;
      this.endDate = endDate;
    },
  },
};
</script>
