from textblob import TextBlob

def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        return {
            "polarity": blob.sentiment.polarity,  # Polarity (-1 to 1)
            "subjectivity": blob.sentiment.subjectivity  # Subjectivity (0 to 1)
        }
    except Exception as e:
        return {"error": f"Error in sentiment analysis: {str(e)}"}
