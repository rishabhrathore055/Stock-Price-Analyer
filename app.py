import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
"""
# Stock Price Analyer
**Shown are the  stock prices of Accenture.**
"""
)
col1,col2 = st.columns(2)
with col1 :
    start_date = st.date_input("Input Staring Date",datetime.date(2023,1,1))
with col2 :
    end_date = st.date_input("Input End Date",datetime.date(2024,2,1))

ticker_symbol = st.text_input(
    "Enter Stock Symbol","ACN",key="placeholder"
)

st.write(f"""
### {ticker_symbol}'s EOD Prices
""")

ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period="1d",
start=f"{start_date}",end=f"{end_date}")

st.dataframe(ticker_df)

st.write("""
## Daily Closing Price Chart
""")
st.line_chart(ticker_df['Close'])

st.write("""
## Volume of Shares traded each day
""")
st.line_chart(ticker_df['Volume'])