<template>
  <v-container fluid>
      
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import {sendPrediction, getPredictions, clearPredictions} from "@/api/main";
import {Result} from "@/types/output";

export default Vue.extend({
  name: "Main",
  data(): {
    log: Result[],
    text: string,
    table: any,
    loading: boolean
    } {
    return {
      log: [],
      text: "",
      table: {
        headers: [
          {
            text: "Text",
            value: "text"
          },
          {
            text: "Label",
            value: "label",
          }
        ]
      },
      loading: false
    };
  },
  async mounted() {
    this.$data.log = await getPredictions();
  },
  methods: {}

});
</script>
