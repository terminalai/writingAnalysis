from flask import Flask, jsonify, request
from flask import session
from flask_cors import CORS
import nltk
from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from bs4 import BeautifulSoup as souper
import requests

def nytimes(url):
    soup = souper(requests.get(url).content, features="lxml")
    title = soup.find("h1")
    title = title.text if title else ""
    text = "\n\n".join([tag.text for tag in soup.findAll("p", {"class":"evys1bk0"})])
    return dict(text=text, title=title)

model_checkpoint = "distilbert-base-uncased"
category_codes = dict(enumerate(
    ['Claim', 'Concluding Statement', 'Counterclaim', 'Evidence', 'Lead', 'Position', 'Rebuttal']))
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
model_path = r"models_gitignored/distilbert-base-uncased-finetuned-sentence-classification/checkpoint-12626"
loaded_model = AutoModelForSequenceClassification.from_pretrained(
    model_path, id2label=category_codes)

pipe = pipeline("text-classification", model=loaded_model, tokenizer=tokenizer)

app = Flask(__name__)
app.secret_key = "super_secret_key"
CORS(app)

def predict(text,**kwargs):
    texts = sentence_tokenizer.tokenize(text)
    #tex = codecs.EncodedFile(BytesIO(bytes(text, "utf-8")), "utf-8").read()
    meta = [{"text": i, **out, **kwargs} for i, out in zip(texts, pipe(texts))]
    #     texts = []
    #     labels = []
    #     for text, label in df.loc[:, :"label"].values:
    #         if len(labels):
    #             if labels[-1] == label:
    #                 texts[-1] += " "+text
    #                 continue

    #         texts.append(text)
    #         labels.append(label)

    #     df = pd.DataFrame({"text":texts, "label":labels})

    
    return meta


@app.route("/api/tasks", methods=["GET"])
def retrieve_data():
  try:
    return jsonify(session["result"])
  except: return jsonify([])

@app.route('/api/task', methods=['POST'])
def input_predict_text():
    text = request.get_json()['text']
    meta = predict(text)
    try: session["result"] += meta
    except: session["result"] = meta
    return jsonify(meta)

@app.route("/api/clear", methods=["GET"])
def clear_session():
  session["result"] = []
  return jsonify([])

@app.route("/api/nytimes", methods=["POST"])
def predict_nytimes():
  url = request.get_json()["url"]
  dat = nytimes(url)
  meta = predict(dat["text"], url=url, title=dat['title'])
  session["nytimes"] = meta
  return jsonify(meta)


if __name__ == '__main__':
    app.run(debug=True)
