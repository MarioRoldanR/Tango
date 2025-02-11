# src/data_ingestion.py

import yfinance as yf
import pandas as pd

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

if __name__ == '__main__':
    # --- Prueba de la función fetch_stock_data ---
    ticker = 'AAPL'
    stock_data = fetch_stock_data(ticker=ticker, period='1y', interval='1d')
    print("\nPrimeras filas de los datos históricos para", ticker)
    print(stock_data.head())

    # --- Prueba de la función fetch_sample_tweets ---
    tweets = fetch_sample_tweets()
    print("\nTweets de ejemplo:")
    for tweet in tweets:
        print("-", tweet)