export class Result {
    text:string;
    output: string;
    model: string;

    constructor(text: string, output: string, model: string) {
        this.text = text;
        this.output = output;
        this.model = model;
    }
}