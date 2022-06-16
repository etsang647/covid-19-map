<template>
  <div class="form">
    <div class="form-input">
      <label for="type">Type</label>
      <select v-model="inputs.dataType">
        <option value="cases">cases</option>
        <option value="deaths">deaths</option>
      </select>
    </div>

    <div class="form-input">
      <label for="date">Start date</label>
      <input type="date" class="date-picker" v-model="inputs.startDate"
      :min="this.defaultDates.min" :max="this.defaultDates.max">
    </div>

    <div class="form-input">
      <label for="date">End date</label>
      <input type="date" class="date-picker" v-model="inputs.endDate"
      :min="this.defaultDates.min" :max="this.defaultDates.max">
    </div>
  </div>
</template>

<script>
export default {
  name: 'Forms',
  data() {
    return {
      inputs: {
        dataType: this.dataType,
        startDate: this.defaultDates.start,
        endDate: this.defaultDates.end,
      },
      errorMsg: '',
    };
  },
  props: {
    dataType: String,
    defaultDates: Object,
  },
  watch: {
    inputs: {
      handler() {
        this.checkForErrors();
        if (this.errorMsg) {
          this.$emit('invalid-input', this.errorMsg);
        } else {
          this.$emit('valid-input', this.inputs);
        }
      },
      deep: true,
    },
  },
  methods: {
    // format date string from yyyy-mm-dd to mm/dd/yyyy
    formatDate(date) {
      const [year, month, day] = date.split('-');
      const newDate = [month, day, year].join('/');
      return newDate;
    },
    dataTypeValid() {
      const { dataType } = this.inputs;
      return dataType === 'cases' || dataType === 'deaths';
    },
    datesWithinRange() {
      const startDate = new Date(this.inputs.startDate);
      const endDate = new Date(this.inputs.endDate);
      const minDate = new Date(this.defaultDates.min);
      const maxDate = new Date(this.defaultDates.max);

      const startDateValid = startDate >= minDate && startDate <= maxDate;
      const endDateValid = endDate >= minDate && endDate <= maxDate;

      return startDateValid && endDateValid;
    },
    datesInOrder() {
      const startDate = new Date(this.inputs.startDate);
      const endDate = new Date(this.inputs.endDate);

      return startDate <= endDate;
    },
    // checks if form inputs are valid and stores relevant error message in this.errorMsg
    checkForErrors() {
      if (!this.dataTypeValid()) {
        this.errorMsg = 'Error: Type value is not "cases" or "deaths"';
      } else if (!this.datesWithinRange()) {
        const minDate = this.formatDate(this.defaultDates.min);
        const maxDate = this.formatDate(this.defaultDates.max);
        this.errorMsg = `Error: Date is outside range [${minDate}, ${maxDate}]`;
      } else if (!this.datesInOrder()) {
        this.errorMsg = 'Error: Start date is later than end date';
      } else {
        this.errorMsg = '';
      }
    },
  },
};
</script>
