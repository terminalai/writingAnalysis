import {Result} from "@/types/output";
import axios from 'axios';

export async function sendPrediction(paragraph: string, model:string) {
  await axios.post('/api/output',
        { text: paragraph, model:model })
        .then(res => {
          console.log(res)
        },
        res => {
          console.log("error")
        })
        .catch(err => {
          console.log(err)
        }) 
}

export async function getPredictions(): Promise<Result[]> {
    try {
        const resp = await axios.get('/api/outputs');
        return (await resp.data) as Result[]
    } catch (err) {
        console.error(err);
        return []
    }

}

export async function clearPredictions(): Promise<Result[]> {
    try {
        const resp = await axios.get('/api/clear');
        return (await resp.data) as Result[]
    } catch (err) {
        console.error(err);
        return []
    }
}