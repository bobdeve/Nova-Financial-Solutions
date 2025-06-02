from textblob import TextBlob

def calculate_sentiment(text):
    """
    Calculate sentiment polarity of given text.
    """
    return TextBlob(text).sentiment.polarity