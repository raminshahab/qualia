<template>
    <div v-if="visible" class="error-dialog">
      <div class="dialog-overlay" @click="closeDialog"></div>
      <div class="dialog-content">
        <h2>Error</h2>
        <p>{{ message }}</p>
        <button @click="closeDialog">Close</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      visible: Boolean,
      message: String,
    },
    methods: {
      closeDialog() {
        this.$emit('close');
      },
    },
  };
  </script>
  
  <style scoped>
  .error-dialog {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .dialog-content {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
  }
  
  .dialog-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  </style>
  