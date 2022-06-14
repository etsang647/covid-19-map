<template>
  <form class="date-and-type">
    <label for="type">Type:</label>
    <select name="" id="" v-model="inputs.dataType">
      <option value="cases">cases</option>
      <option value="deaths">deaths</option>
    </select>

    <label for="date">Start date:</label>
    <input type="date" class="date-picker" v-model="inputs.startDate"
    :min="this.dates.min" :max="this.dates.max">

    <label for="date">End date:</label>
    <input type="date" class="date-picker" v-model="inputs.endDate"
    :min="this.dates.min" :max="this.dates.max">
  </form>
</template>

<script>
export default {
  name: 'Forms',
  data() {
    return {
      inputs: {
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
        this.$emit('input-changed', this.inputs);
      },
      deep: true,
    },
  },
};
</script>
