import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple StockPrice App

Shown are are the stock **closing price** and ***volume*** of Reliance Industries Limited(RELIANCE. NS) !

""")

#DEFINING THE TICKER sYMBOL
tickerSymbol = 'RELIANCE.NS'
#getting Data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical data on this ticker 
tickerDf = tickerData.history(period='1d',start = '2005-5-31',end = '2021-4-30')

st.write("""
## Closing Price
""")
#open High low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)