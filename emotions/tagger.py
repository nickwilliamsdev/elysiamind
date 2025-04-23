from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class EmotionTagger:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def tag(self, text):
        scores = self.analyzer.polarity_scores(text)
        compound = scores["compound"]
        if compound >= 0.5:
            return "joy"
        elif compound >= 0.1:
            return "warmth"
        elif compound <= -0.5:
            return "sadness"
        elif compound <= -0.1:
            return "frustration"
        else:
            return "neutral"

    def significance_score(self, emotion):
        weights = {
            "joy": 0.9,
            "warmth": 0.7,
            "sadness": 0.8,
            "frustration": 0.6,
            "neutral": 0.4
        }
        return weights.get(emotion, 0.5)
