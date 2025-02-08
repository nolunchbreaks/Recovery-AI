import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('punkt')  # Download NLP tokenizer

class EmotionalStateAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def predict(self, user_input: str) -> dict:
        sentiment_scores = self.analyzer.polarity_scores(user_input)
        
        # Mapping sentiment to emotions
        return {
            'sadness': abs(sentiment_scores['neg']),
            'anxiety': abs(sentiment_scores['neu']),  
            'hope': abs(sentiment_scores['pos']),
            'overall_score': (sentiment_scores['compound'] + 1) / 2  # Normalize [-1,1] to [0,1]
        }
