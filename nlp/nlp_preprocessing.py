import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess_text(text: str) -> str:
    """
    Preprocess the text by removing punctuation, converting to lowercase, and tokenizing.

    Args:
        text (str): The input text.

    Returns:
        str: The preprocessed text.
    """
    # Remove punctuation
    text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)

    # Convert to lowercase
    text = text.lower()

    # Tokenize
    words = nltk.word_tokenize(text)

    return ' '.join(words)

def clean_text(text: str) -> str:
    """
    Clean the text by removing stopwords and lemmatizing.

    Args:
        text (str): The input text.

    Returns:
        str: The cleaned text.
    """
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in text.split() if word not in stop_words]

    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    return ' '.join(words)
