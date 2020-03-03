<template>
  <v-app>
    <v-card width="600" class="mx-auto mt-5">
      <v-card-title>
        <h1 class="display-1">Reverse string</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            label="Enter string here"
            prepend-icon="mdi-alien-outline"
            v-model="newString"
          ></v-text-field>
        </v-form>
        <div class="text--primary">{{ newString }}</div>
        <div class="text--primary">{{ 'reversed: ' + reversedString }}</div>
      </v-card-text>
      <v-card-actions>
        <v-btn color="success" @click="reverse">Reverse</v-btn>
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
    counter: 0
  }),
  methods: {
    greet() {
      alert("op op op");
    },
    reverse() {
      axios
        .get("http://www.localhost:5000/reverse", {
          params: { line: this.newString }
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
