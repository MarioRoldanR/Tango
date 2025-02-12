# src/dashboard.py

import streamlit as st

def main():
    # Título y descripción
    st.title("Dashboard Tango")
    st.subheader("Configuración de Parámetros para el Análisis")
    st.write("Defina los parámetros a utilizar en el análisis de datos.")

    # Entrada de tickers: se espera que el usuario ingrese tickers separados por comas.
    tickers_input = st.text_input(
        "Ingrese los tickers a analizar (separados por comas):", 
        value="AAPL, MSFT, GOOGL"
    )
    # Convertir la cadena de texto en una lista de tickers, eliminando espacios innecesarios.
    tickers = [ticker.strip().upper() for ticker in tickers_input.split(",") if ticker.strip()]
    st.write("Tickers seleccionados:", tickers)

    # Selección del período para la descarga de datos
    period = st.selectbox("Seleccione el período de análisis:", 
                           options=["1mo", "3mo", "6mo", "1y", "5y", "max"], index=3)
    st.write("Período seleccionado:", period)

    # Selección del intervalo de datos
    interval = st.selectbox("Seleccione el intervalo de datos:", 
                             options=["1d", "1wk", "1mo"], index=0)
    st.write("Intervalo seleccionado:", interval)

    # Botón para iniciar el análisis (placeholder por ahora)
    if st.button("Iniciar Análisis"):
        st.success("Análisis iniciado para: " + ", ".join(tickers))
        st.info("Esta funcionalidad se integrará con los módulos de ingesta y análisis en versiones posteriores.")

if __name__ == "__main__":
    main()