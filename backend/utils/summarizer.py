import nltk
from nltk.tokenize import sent_tokenize

# Ensure the punkt resource is available
nltk.download('all')


def summarize_text(text, num_sentences=3):
    try:
        sentences = sent_tokenize(text)
        return ' '.join(sentences[:num_sentences]) if sentences else "No content to summarize."
    except Exception as e:
        return f"Error in summarization: {str(e)}"
