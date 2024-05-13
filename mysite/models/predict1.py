import pandas as pd
import glob
# import seaborn as sns
import numpy as np
import string
from string import digits, punctuation
import re
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset, RandomSampler, SequentialSampler
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import naive_bayes, svm
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split
from vncorenlp import VnCoreNLP
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix
from transformers import AutoTokenizer, AdamW, get_linear_schedule_with_warmup ,RobertaForSequenceClassification
import joblib
from text_processing import word_segmentation, clean_text

# device = "cuda:0" if torch.cuda.is_available() else "cpu"

device = "cpu"

# Define the model name/path
model_name = "phobert_sentiment_analysis"

# Load the model
model = RobertaForSequenceClassification.from_pretrained(model_name)

# Load the tokenizer as well
tokenizer = AutoTokenizer.from_pretrained(model_name)

def preprocessing_text(text):
    cleaned_text = clean_text(text)
    # cleaned_text = cleaned_text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    segmentented_text = word_segmentation(cleaned_text)
    
    return segmentented_text

def predict_sentiment(model, tokenizer, text):
    # Clean the text
    segmentented_text = preprocessing_text(text)
    # Tokenize the cleaned segmented text
    inputs = tokenizer(segmentented_text, truncation=True, padding=True, max_length=256, return_tensors="pt")

    # Ensure inputs are on the same device as the model
    device = next(model.parameters()).device
    inputs = {key: val.to(device) for key, val in inputs.items()}

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    return predicted_class

# Example usage
while True:
    # raw_text = "Thời tiết rất đẹp"
    raw_text = input("Enter a text (type 'quit()' to exit): ")
    if raw_text.lower() == 'quit()':
        break
    predicted_sentiment = predict_sentiment(model, tokenizer, raw_text)
    print("Predicted sentiment:", "Positive" if predicted_sentiment == 1 else "Negative")
