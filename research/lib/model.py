import nltk
import pandas as pd
import numpy as np
import torch

from datasets import Dataset

category_codes = {0: 'Claim',
 1: 'Concluding Statement',
 2: 'Counterclaim',
 3: 'Evidence',
 4: 'Lead',
 5: 'Position',
 6: 'Rebuttal'}

nltk.download('punkt')
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def pseudoLabel(text, tokenizer, model):
    """
    text is a pd.Series variable containing paragraphs.
    """
    
    sentences = text.apply(sentence_tokenizer.tokenize).explode()
    print(f"{len(sentences)} sentences split")
    
    def tokenize_and_encode(examples):
        return tokenizer(examples['0'], padding=True, truncation=True)

    dataset = Dataset.from_pandas(pd.DataFrame(sentences))
    dataset = dataset.map(tokenize_and_encode, batched=True, remove_columns=["0"])
    dataset.set_format(type='torch', columns=['input_ids', 'attention_mask'])
    
    def model_prediction(examples):
        torch.cuda.empty_cache()
        print(examples['attention_mask'])
        with torch.no_grad():
            outputs = model(input_ids=examples['input_ids'].to(model.device),
                            attention_mask=examples['attention_mask'].to(model.device))
        return {"labels":outputs.logits.cpu().detach().numpy()}
    
    dataset = dataset.map(model_prediction, batched=True, batch_size=150)
    
    return dataset

