import {Result} from "@/types/output";

export async function getPredictions(paragraph: string): Promise<Result[]> {
  return await fetch('https://httpbin.org/post', {
    method: 'POST',
    headers: {
      'Accept': 'application/json, text/plain, */*',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({text: paragraph})
  }).then(res => res.json())
    .then(res => console.log(res)) as Result[];
}