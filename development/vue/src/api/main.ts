import {Result} from "@/types/output";
import axios from 'axios';

export async function sendPrediction(paragraph: string) {
  await axios.post('/api/task',
        { text: paragraph })
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
        const resp = await axios.get('/api/tasks');
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

export async function predictNYT(url: string) {
  await axios.post('/api/task',
        { url: url })
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