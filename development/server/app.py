from flask import Flask, jsonify, request
from flask import session
from flask_cors import CORS
import nltk
from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification



options = {
    "DistilBERT": dict(tokenizer="distilbert-base-uncased", path=r"models_gitignored/distilbert/checkpoint-50504"),
    "BERT": dict(tokenizer="bert-base-uncased", path=r"models_gitignored/bert/checkpoint-75756"),
    "DistilGPT2": dict(tokenizer="distilgpt2", path=r"models_gitignored/distilgpt2/checkpoint-252515"),
    "Teacher RoBERTa": dict(tokenizer="roberta-base", path=r"models_gitignored/roberta_base/checkpoint-75756"),
    "Student RoBERTa 0": dict(tokenizer="roberta-base", path=r"models_gitignored/roberta_noisy_iterations/iter0/checkpoint-65255"),
    "Student RoBERTa 1": dict(tokenizer="roberta-base", path=r"models_gitignored/roberta_noisy_iterations/iter1/checkpoint-65255"),
    "Student RoBERTa 2": dict(tokenizer="roberta-base", path=r"models_gitignored/roberta_noisy_iterations/iter2/checkpoint-65255"),
}

category_codes = dict(enumerate(['Claim', 'Concluding Statement', 'Counterclaim', 'Evidence', 'Lead', 'Position', 'Rebuttal']))
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

app = Flask(__name__)
app.secret_key = "super_secret_key"
CORS(app)

def predict(text, tokenizer, path, **kwargs):
    tokenizerer = AutoTokenizer.from_pretrained(tokenizer, use_fast=True)
    loaded_model = AutoModelForSequenceClassification.from_pretrained(path, id2label=category_codes)
    pipe = pipeline("text-classification", model=loaded_model, tokenizer=tokenizerer)
    texts = sentence_tokenizer.tokenize(text)
    meta = [{"text": i, **out, **kwargs} for i, out in zip(texts, pipe(texts))]
    del tokenizerer
    del loaded_model
    return meta

@app.route("/api/outputs", methods=["GET"])
def retrieve_data():
  try: return jsonify(session["result"])
  except: return jsonify([])

@app.route('/api/output', methods=['POST'])
def input_predict_text():
    text = request.get_json()['text']
    if text.strip() == "": return jsonify([])
    model = request.get_json()["model"]
    meta = predict(text, **options[model], model=model)
    try: session["result"] += meta
    except: session["result"] = meta
    return jsonify(meta)

@app.route("/api/clear", methods=["GET"])
def clear_session():
  session["result"] = []
  return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
