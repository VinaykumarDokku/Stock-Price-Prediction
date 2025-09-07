@'
# Stock Price Prediction with RNN (AAPL)

A small educational project that trains a simple Recurrent Neural Network (RNN) to predict Apple (AAPL) closing prices using historical data from Yahoo Finance.

## Quick summary
- Data: downloaded with `yfinance` (2015–2024)
- Preprocessing: `MinMaxScaler` and 10-day sliding windows
- Model: `SimpleRNN(64) -> Dense(1)` (Keras/TensorFlow)
- Output: plots comparing true vs predicted prices

## Run notebook:

jupyter notebook stock_price_prediction.ipynb

## Run Notebook in Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1vxT42UweHOPaQ2f-oQQb9yEfYv8yzTd6)
