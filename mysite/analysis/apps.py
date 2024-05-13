from django.apps import AppConfig
from transformers import AutoTokenizer ,RobertaForSequenceClassification


class AnalysisConfig(AppConfig):
    name = 'analysis'

    def ready(self):
        # Define the model name/path
        model_name = "/mnt/d/ALLIN/Diploma/new diploma/mysite/models/phobert_sentiment_analysis_new"

        # Load the model
        self.model = RobertaForSequenceClassification.from_pretrained(model_name)

        # Load the tokenizer as well
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Set device
        self.device = "cpu"
