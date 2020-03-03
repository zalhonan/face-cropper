<template>
  <v-app>
    <v-card width="600" class="mx-auto mt-5">
      <v-card-title>
        <h1 class="display-1">Upload file to server</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-file-input v-model="file" label="Select Image File..."></v-file-input>
        </v-form>
        <div class="text--primary">{{ newString }}</div>
        <div class="text--primary">{{ 'responce from server: ' + reversedString }}</div>
      </v-card-text>
      <v-card-actions>
        <v-btn color="success" @click="onUpload">Upload</v-btn>
      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  name: "App",

  data: () => ({
    showPassword: false,
    newString: "",
    reversedString: "responce will be here",
    counter: 0,
    file: null,
    imageUrl: null
  }),
  methods: {
    greet() {
      alert("op op op");
    },
    onUpload() {
      console.log(this.file.name);

      axios
        .post("http://www.localhost:5000/file", this.file, {
          headers: {
            "Content-Type": "image/jpeg"
          }
        })
        .then(response => {
          console.log(response.data);
          this.reversedString = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>