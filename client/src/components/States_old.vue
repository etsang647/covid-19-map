<template>
  <object id="svg-object" :data="svgPath" type="image/svg+xml" ref="map"></object>
</template>

<script>
export default {
  name: 'States',
  data() {
    return {
      // eslint-disable-next-line global-require
      svgPath: require('@/assets/usa.svg'),
      dates: {},
      states: null,
      startDate: '',
      endDate: '',
    };
  },
  mounted() {
    fetch('http://localhost:5000/data')
      .then((res) => res.json())
      .then((data) => {
        this.dates = data.dates;
        this.startUp();
      });
  },
  watch: {
    start: {
      handler() {
        this.states.forEach((state) => {
          console.log(state.classList);
        });
      },
    },
  },
  props: ['response', 'start', 'date', 'type'],
  methods: {
    startUp() {
      const mapDocument = this.$refs.map.contentDocument;
      this.states = mapDocument.querySelectorAll('path');
      this.states.forEach((state) => {
        const stateName = state.getAttribute('name');
        state.classList.add(this.getClass(stateName));
        console.log(state.classList);
        state.addEventListener('mouseover', this.getNumber);
        state.addEventListener('mouseleave', this.unhover);
      });
    },
    // get html class (i.e. color) for state 'name'
    getClass(name) {
      // if date is invalid, determine class for 0 cases/deaths
      if (!this.isValidDate(this.start) || !this.isValidDate(this.date)) {
        this.$emit('valid-date', false);
        return this.determineClass(0);
      }
      // otherwise if date is valid, determine class for # of cases/deaths on that day
      this.$emit('valid-date', true);
      const startDate = this.dates[this.start];
      const date = this.dates[this.date];
      let startNumber;
      let number;

      if (name in startDate) startNumber = startDate[name][this.type];
      else startNumber = 0;
      if (name in date) number = date[name][this.type];
      else number = 0; // if state not found in server response, set its number to 0

      return this.determineClass(number - startNumber);
    },
    // determines class i.e. color of state based on number of cases/deaths
    determineClass(count) {
      let classStr;
      const number = Math.abs(count);

      if (number === 0) classStr = 'class-0';
      else if (number >= 1 && number <= 9) classStr = 'class-1';
      else if (number >= 10 && number <= 99) classStr = 'class-2';
      else if (number >= 100 && number <= 999) classStr = 'class-3';
      else if (number >= 1000 && number <= 9999) classStr = 'class-4';
      else if (number >= 10000 && number <= 99999) classStr = 'class-5';
      else if (number >= 100000 && number <= 999999) classStr = 'class-6';
      else if (number >= 1000000 && number <= 9999999) classStr = 'class-7';
      else classStr = 'class-8';

      return classStr;
    },
    getNumber(e) {
      this.showNumber(e.target.getAttribute('name'));
    },
    // emit case/death numbers for state 'name'
    showNumber(name) {
      // 0 if invalid date
      if (!this.isValidDate(this.start) || !this.isValidDate(this.date)) {
        const str = `${name}: 0 ${this.type}`;
        this.$emit('hover-state', str);
        return;
      }
      const startDate = this.dates[this.start];
      const date = this.dates[this.date];
      let startNumber;
      let number;

      if (name in startDate) startNumber = startDate[name][this.type];
      else startNumber = 0;
      if (name in date) number = date[name][this.type];
      else number = 0; // if state not found in server response, set its number to 0

      const str = `${name}: ${number - startNumber} ${this.type}`;
      this.$emit('hover-state', str);
    },
    unhover() {
      this.$emit('unhover-state');
    },
    // checks if selected date is within bounds of dataset range
    isValidDate(date) {
      const startDate = new Date(2020, 0, 21); // start = 2020-01-21
      startDate.setUTCHours(0);

      const datesArray = Object.keys(this.dates);
      const endDate = new Date(datesArray[datesArray.length - 1]);
      endDate.setUTCHours(0, 0, 0, 0);

      const selectedDate = new Date(date);
      selectedDate.setUTCHours(0, 0, 0, 0);

      return selectedDate >= startDate && selectedDate <= endDate;
    },
  },
};
</script>
