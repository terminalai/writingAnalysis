<template>
  <v-container fluid>
    <v-row justify="center" >
      <v-col cols='3' align-self="center">
        <v-combobox
          outlined
          dense
          v-model="selection"
          label="Select Model"
          :items="items"
        ></v-combobox>
      </v-col>
      <v-col align-self="center" cols="1">
        <v-row>
          <v-col>
        <v-btn @click="submit" style="display: block; margin: auto" row-height="5" color="primary"
        :loading="loading">Submit</v-btn>
        </v-col>
        <v-col>
        <v-btn @click="clear" style="display: block; margin: auto" row-height="5"
        :loading="loading">Clear</v-btn>
        </v-col>
        </v-row>
      </v-col>
    </v-row>

    <v-row justify='center'>
      <v-col cols='10' align-self="center">
        <v-textarea
          outlined
          auto-grow
          name="input-7-1"
          label="Text to Analyse"
          v-model="text"
          counter
          row-height="10"
        ></v-textarea>
      </v-col>
        </v-row>
    <v-data-table :headers="table.headers" :items="log" row-height="15">
    </v-data-table>
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
    selection: string,
    items: string[],
    loading: boolean
    } {
    return {
      log: [],
      text: "",
      selection: "",
      items: [
        'DistilBERT',
        'BERT',
        'DistilGPT2',
        'Teacher RoBERTa',
        'Student RoBERTa 0',
        'Student RoBERTa 1',
        'Student RoBERTa 2',
      ],
      table: {
        headers: [
          {
            text: "Text",
            value: "text"
          },
          {
            text: "Label",
            value: "label",
          },
          {
            text: "Model",
            value: "model",
          }
        ]
      },
      loading: false
    };
  },
  async mounted() {
    this.$data.log = await getPredictions();
  },
  methods: {
    async submit() {
      this.loading = true;
      await sendPrediction(this.text, this.selection);
      this.$data.log = await getPredictions();
      this.loading = false;
    },
    async clear() {
      await clearPredictions();
      this.$data.log = await getPredictions();
    }
  }

});
</script>
<style>
 // Hide scrollbar for Chrome, Safari and Opera */
.hide-scrollbar::-webkit-scrollbar {
    display: none;
  }

// Hide scrollbar for IE, Edge and Firefox */
.hide-scrollbar {
   -ms-overflow-style: none;  /* IE and Edge */
   scrollbar-width: none;  /* Firefox */
}

.v-input.v-text-field.v-textarea .v-text-field__slot {
  padding-right: 1px;
  padding-bottom: 1px
}
</style>