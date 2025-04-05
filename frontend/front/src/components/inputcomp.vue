<template>
    <input
      type="text"
      v-model="localValue"
      @keyup.enter="removeFocus"
      ref="inputRef"
    />
  </template>
  
  <script>
  export default {
    name: 'inputcomp',
    props: {
      modelValue: String
    },
    emits: ['update:modelValue'],
    data() {
      return {
        localValue: this.modelValue
      }
    },
    watch: {
      modelValue(newVal) {
        this.localValue = newVal
      }
    },
    methods: {
      removeFocus() {
        this.$refs.inputRef.blur();
      }
    }
  }
  </script>
  
  <style scoped>
  input {
    height: 30px;
    width: 60px;
    margin: 5px;
    background-color: #2D2D2D;
    border: none;
    text-align: center;
    border-radius: 5px;
    font-size: 16px;
    color: white;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    padding-inline: 5px;
  }
  </style>
  