import nltk
import pandas as pd
import numpy as np


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
    encoded_inputs = tokenizer(sentences.to_list(), return_tensors="pt", padding=True,
                               truncation=True, max_length=512)
    outputs = model(**encoded_inputs)
    logits_df = pd.DataFrame([(x,) for x in outputs.logits.detach().numpy()])
    
    return pd.concat([sentences, logits_df], axis=1).rename(columns={"0":"text", "1":"labels"})

