<template>
  <div class="form">
    <div class="form-input">
      <label for="type">Type</label>
      <select name="" id="" v-model="inputs.dataType">
        <option value="cases">cases</option>
        <option value="deaths">deaths</option>
      </select>
    </div>

    <div class="form-input">
      <label for="date">Start date</label>
      <input type="date" class="date-picker" v-model="inputs.startDate"
      :min="this.dates.min" :max="this.dates.max">
    </div>

    <div class="form-input">
      <label for="date">End date</label>
      <input type="date" class="date-picker" v-model="inputs.endDate"
      :min="this.dates.min" :max="this.dates.max">
    </div>
  </div>
</template>

<script>
export default {
  name: 'Forms',
  data() {
    return {
      inputs: {
        // default values from parent
        dataType: this.dataType,
        startDate: this.dates.start,
        endDate: this.dates.end,
      },
      errorMsg: '',
    };
  },
  props: {
    dataType: String,
    dates: Object,
  },
  watch: {
    inputs: {
      handler() {
        if (this.checkForErrors()) {
          this.$emit('error-changed', this.errorMsg);
        } else {
          this.$emit('input-changed', this.inputs);
        }
      },
      deep: true,
    },
  },
  methods: {
    dataTypeValid() {
      const { dataType } = this.inputs;
      return dataType === 'cases' || dataType === 'deaths';
    },
    datesWithinRange() {
      const startDate = new Date(this.inputs.startDate);
      const endDate = new Date(this.inputs.endDate);
      const minDate = new Date(this.dates.min);
      const maxDate = new Date(this.dates.max);

      const startDateValid = startDate >= minDate && startDate <= maxDate;
      const endDateValid = endDate >= minDate && endDate <= maxDate;

      return startDateValid && endDateValid;
    },
    datesInOrder() {
      const startDate = new Date(this.inputs.startDate);
      const endDate = new Date(this.inputs.endDate);

      return startDate <= endDate;
    },
    checkForErrors() {
      if (!this.dataTypeValid()) {
        this.errorMsg = 'Error: Type value is not "cases" or "deaths"';
      } else if (!this.datesWithinRange()) {
        const minDate = this.formatDate(this.dates.min);
        const maxDate = this.formatDate(this.dates.max);
        this.errorMsg = `Error: Date is outside range [${minDate}, ${maxDate}]`;
      } else if (!this.datesInOrder()) {
        this.errorMsg = 'Error: Start date is later than end date';
      } else {
        this.errorMsg = '';
      }
      return this.errorMsg;
    },
    // format date string from yyyy-mm-dd to mm/dd/yyyy
    formatDate(date) {
      const [year, month, day] = date.split('-');
      const newDate = [month, day, year].join('/');
      return newDate;
    },
  },
};
</script>
