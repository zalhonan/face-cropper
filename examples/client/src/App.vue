<template>
  <div id="app">
    <v-app>
      <v-app-bar color="primary" dark >
        <v-toolbar-title>Choose app</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn :to="{ name: 'LatestMovie' }" color="purple" class="mr-2"> Movies</v-btn>
        <v-btn :to="{ name: 'ReverseString' }" color="purple" class="mr-2"> Reverse</v-btn>
        <v-btn :to="{ name: 'FileUpload' }" color="purple" class="mr-2"> File Uploads</v-btn>
      </v-app-bar>
      <router-view  />
    </v-app>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
</style>
