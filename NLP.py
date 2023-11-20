from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity (ranges from -1 to 1)
    sentiment_polarity = blob.sentiment.polarity
    
    # Classify the sentiment
    if sentiment_polarity > 0:
        sentiment = 'Positive'
    elif sentiment_polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, sentiment_polarity

# Example usage
text_to_analyze1 = "Python is a great language!"
text_to_analyze2 = "Python is a terrible language!"
text_to_analyze3 = "python is a programming language!"
sentiment_result1, polarity1 = analyze_sentiment(text_to_analyze1)
sentiment_result2, polarity2 = analyze_sentiment(text_to_analyze2)
sentiment_result3, polarity3 = analyze_sentiment(text_to_analyze3)

print(f"Text: {text_to_analyze1}")
print(f"Sentiment: {sentiment_result1}")
print(f"Polarity: {polarity1}")
print()
print(f"Text: {text_to_analyze2}")
print(f"Sentiment: {sentiment_result2}")
print(f"Polarity: {polarity2}")
print()
print(f"Text: {text_to_analyze3}")
print(f"Sentiment: {sentiment_result3}")
print(f"Polarity: {polarity3}")
