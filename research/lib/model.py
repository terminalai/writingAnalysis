import nltk

from tqdm.auto import tqdm

from sklearn.model_selection import train_test_split
from sklearn.metrics import cohen_kappa_score

import pandas as pd
import numpy as np
import logging
from glob import glob
from os import path

from IPython.display import HTML, display

import torch

from transformers import pipeline
from transformers import AutoTokenizer
from transformers import DataCollatorWithPadding
from transformers import AutoModelForSequenceClassification, TrainingArguments
from transformers import PreTrainedModel
from transformers.pipelines.pt_utils import KeyDataset

category_codes = {0: 'Claim',
 1: 'Concluding Statement',
 2: 'Counterclaim',
 3: 'Evidence',
 4: 'Lead',
 5: 'Position',
 6: 'Rebuttal'}
labels = list(zip(*category_codes.items()))[1]


sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def predictLogits(text, tokenizer, model):
    return {t:dict(zip(labels, model(**tokenizer(t, return_tensors="pt")).logits[0].tolist())) for t in sentence_tokenizer.tokenize(text)}

def predictLabel(logits):
    return sorted(logits, key=lambda x:logits[x])[-1]

