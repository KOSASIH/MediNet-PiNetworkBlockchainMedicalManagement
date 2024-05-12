import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from gensim import corpora, models

def analyze_sentiment(text: str) -> dict:
    """
    Analyze the sentiment of the text using the NLTK SentimentIntensityAnalyzer.

    Args:
        text (str): The input text.

    Returns:
        dict: The sentiment analysis results.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    return sentiment_scores

def topic_modeling(corpus: list, num_topics: int) -> tuple:
    """
    Perform topic modeling on the input corpus using Gensim LDA.

    Args:
        corpus (list): The input corpus.
        num_topics (int): The number of topics to extract.

    Returns:
        tuple: The topic modeling results, including the topics and the topic proportions.
    """
    # Create a dictionary and corpus
    id2word = corpora.Dictionary(corpus)
    corpus_tfidf = [id2word.doc2bow(text) for text in corpus]

    # Train the LDA model
    lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=id2word, passes=10)

    # Get the topics and topic proportions
    topics = lda.print_topics(num_words=5)
    topic_proportions = [lda.get_document_topics(bow) for bow in corpus_tfidf]

    return topics, topic_proportions
