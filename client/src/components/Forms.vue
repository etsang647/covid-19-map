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
    };
  },
  props: {
    dataType: String,
    dates: Object,
  },
  watch: {
    inputs: {
      handler() {
        if (!this.dataTypeValid()) {
          this.$emit('data-type-invalid');
        } else if (!this.datesWithinRange()) {
          this.$emit('date-out-of-bounds');
        } else if (!this.datesInOrder()) {
          this.$emit('date-out-of-order');
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
  },
};
</script>
