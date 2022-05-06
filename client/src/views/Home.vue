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
    <Map id="map" :date="date" :type="type" />
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
      date: this.getEndDate(),
      type: 'cases',
      endDate: this.getEndDate(),
    };
  },
  methods: {
    formatDate(date) {
      const selectedDate = new Date(date);

      selectedDate.setUTCHours(0, 0, 0, 0);

      const formattedDate = selectedDate.toLocaleString('en-US', {
        month: '2-digit',
        day: '2-digit',
        year: 'numeric',
        timeZone: 'UTC',
      });
      return formattedDate;
    },
    getEndDate() {
      let date = new Date();
      date.setDate(date.getDate() - 1); // yesterday's date
      const offset = date.getTimezoneOffset();
      date = new Date(date.getTime() - (offset * 60 * 1000));
      console.log('is this working');
      return date.toISOString().split('T')[0];
    },
  },
};
</script>
