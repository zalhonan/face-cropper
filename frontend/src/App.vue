<template>
  <v-app>
    <v-card width="600" class="mx-auto mt-5">
      <v-card-title>
        <h1 class="display-1">Upload your image to crop faces</h1>
      </v-card-title>
      <v-card-text>
        <v-file-input show-size label="Choose your image" prepend-icon="mdi-camera"></v-file-input>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn right color="success" @click="importTxt">Upload</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    showPassword: false,
    chosenfile: null,
    data: null
  }),
  methods: {
    importTxt() {
      console.log("oops");
    }
  }
};
</script>
