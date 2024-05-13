from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User #####
from django.apps import apps
import torch
from .text_processing import word_segmentation, clean_text


def index(request):
    return HttpResponse("Hello, world.")

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



def get_sentiment(request):
    par = request.GET.get('par', '')
    # Access the AnalysisConfig instance
    analysis_config = apps.get_app_config('analysis')

    # Access model and tokenizer attributes from AnalysisConfig instance
    model = analysis_config.model
    tokenizer = analysis_config.tokenizer
    
    # Check if model and tokenizer are initialized
    if model is None or tokenizer is None:
        return HttpResponse('Model and tokenizer not initialized.')

    predicted_sentiment = predict_sentiment(model, tokenizer, par)
    print('par:', par)
    print(predicted_sentiment)
    return HttpResponse(predicted_sentiment)
