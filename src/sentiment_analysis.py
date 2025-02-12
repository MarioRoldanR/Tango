# src/sentiment_analysis.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(tweets):
    """
    Analiza el sentimiento de una lista de tweets usando VADER.
    
    :param tweets: Lista de strings (tweets o noticias)
    :return: Diccionario con el promedio de sentimiento y una lista de scores individuales
    """
    analyzer = SentimentIntensityAnalyzer()
    scores = [analyzer.polarity_scores(tweet)["compound"] for tweet in tweets]
    
    # Calcular promedio del sentimiento
    avg_score = sum(scores) / len(scores) if scores else 0

    return {"average_sentiment": avg_score, "individual_scores": scores}

if __name__ == '__main__':
    # Prueba con tweets de ejemplo
    sample_tweets = [
        "Great earnings report! The company is performing well.",
        "Terrible customer service. I wouldn't invest in this company.",
        "The stock seems overvalued at this point.",
        "Innovative product launch boosts the company's prospects.",
        "Not sure if the current trends will continue."
    ]

    sentiment_result = analyze_sentiment(sample_tweets)
    
    print("\nAnálisis de Sentimiento:")
    print(f"Sentimiento Promedio: {sentiment_result['average_sentiment']:.3f}")
    print("Scores Individuales:", sentiment_result["individual_scores"])