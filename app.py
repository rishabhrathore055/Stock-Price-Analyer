import pandas as pd
import streamlit as st
import yfinance as yf
# from yahoofinancials import YahooFinancials

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
## Highest Prices thought a day
""")
st.line_chart(ticker_df['High'])

st.write("""
## Volume of Shares traded each day
""")
st.line_chart(ticker_df['Volume'])


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
footer="""<style>
a:link , a:visited{
color: yellow;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: white;
# background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
color: white;
text-align: center;
text-size: 30px;
}
</style>
<div class="footer">
<p>Developed ❤ by Rishabh <a style='display: block; text-align: center;' href="https://www.twitter.com/rishabh_55/" target="_blank">Rishabh Rathore</a></p>
</div>

"""
st.markdown(footer,unsafe_allow_html=True)