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

labels = list(zip(*category_codes.items()))[1]

sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def pseudoLabel(text, tokenizer, model):
    """
    text is a pd.Series variable containing paragraphs.
    """
    
    sentences = text.apply(sentence_tokenizer.tokenize).explode()
    
    tokenized = sentences.apply(lambda s: tokenizer(s, return_tensors="pt", truncation=True, max_length = 514))
    
    logits = tokenized.apply(lambda t: pd.Series(dict(zip(labels, model(**t).logits[0].tolist()))))
    
    category = logits.apply(lambda l: labels[np.argmax(l)], axis=1)
    
    #print(text, sentences, logits, category, sep="\n\n\n")
    
    return pd.concat([text, sentences, logits, category], axis=1).rename(columns={0:"text", 1:"sentence", 2:"category"})
