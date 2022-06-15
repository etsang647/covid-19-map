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
      :min="this.dates.min" :max="inputs.endDate">
    </div>

    <div class="form-input">
      <label for="date">End date</label>
      <input type="date" class="date-picker" v-model="inputs.endDate"
      :min="inputs.startDate" :max="this.dates.max">
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
    };
  },
  props: {
    dataType: String,
    dates: Object,
  },
  watch: {
    inputs: {
      handler() {
        if (this.checkDates()) {
          this.$emit('input-changed', this.inputs);
        } else {
          this.$emit('invalid-date');
        }
      },
      deep: true,
    },
  },
  methods: {
    checkDates() {
      const startDate = new Date(this.inputs.startDate);
      const endDate = new Date(this.inputs.endDate);
      const minDate = new Date(this.dates.min);
      const maxDate = new Date(this.dates.max);

      const startDateValid = startDate >= minDate && startDate <= maxDate;
      const endDateValid = endDate >= minDate && endDate <= maxDate;

      return startDateValid && endDateValid;
    },
  },
};
</script>
