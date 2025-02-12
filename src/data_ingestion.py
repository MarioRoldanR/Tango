# src/data_ingestion.py

import yfinance as yf
import pandas as pd
from src.sentiment_analysis import analyze_sentiment

def fetch_stock_data(ticker='AAPL', period='1y', interval='1d'):
    """
    Descarga datos históricos de un ticker usando yfinance.
    
    :param ticker: Símbolo del activo, por ejemplo 'AAPL'.
    :param period: Periodo de tiempo a descargar (por ejemplo, '1y' para un año).
    :param interval: Intervalo entre datos (por ejemplo, '1d' para diario).
    :return: DataFrame con los datos históricos.
    """
    print(f"Descargando datos para {ticker} durante {period} con intervalo {interval}...")
    data = yf.download(ticker, period=period, interval=interval)
    return data

def fetch_sample_tweets():
    """
    Simula la recolección de tweets para análisis de sentimiento.
    
    :return: Lista de tweets de ejemplo.
    """
    tweets = [
        "Great earnings report! The company is performing well.",
        "Not impressed with today's performance.",
        "Stock seems overvalued according to some experts.",
        "New product launch boosts investor confidence.",
        "Uncertain market conditions ahead."
    ]
    return tweets

def fetch_stock_data_with_sentiment(ticker='AAPL', period='1y', interval='1d'):
    """
    Descarga datos financieros y obtiene el sentimiento del mercado basado en tweets de ejemplo.
    
    :param ticker: Símbolo del activo
    :param period: Período de tiempo
    :param interval: Intervalo de los datos
    :return: DataFrame con datos de mercado y sentimiento
    """
    stock_data = fetch_stock_data(ticker, period, interval)
    tweets = fetch_sample_tweets()
    sentiment = analyze_sentiment(tweets)
    
    # Agregar sentimiento al DataFrame
    stock_data["Sentiment"] = sentiment["average_sentiment"]
    
    return stock_data

if __name__ == '__main__':
    ticker = 'AAPL'
    stock_data = fetch_stock_data_with_sentiment(ticker)
    
    print("\nPrimeras filas de los datos históricos con sentimiento:")
    print(stock_data.head())