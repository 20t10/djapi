<template>
  <div class="example">
    <h1>This is an example page</h1>
    <h4> {{ message }}</h4>
  </div>
</template>
<script>
export default {
    name: "example",
    data() {
        return {
          message: "Hola view"
        }
    }
}
</script>
<style>
h1{
  color: red;
}
</style>
