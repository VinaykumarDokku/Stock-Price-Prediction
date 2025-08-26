@'
# Stock Price Prediction with RNN (AAPL)

A small educational project that trains a simple Recurrent Neural Network (RNN) to predict Apple (AAPL) closing prices using historical data from Yahoo Finance.

## Quick summary
- Data: downloaded with `yfinance` (2015–2024)
- Preprocessing: `MinMaxScaler` and 10-day sliding windows
- Model: `SimpleRNN(64) -> Dense(1)` (Keras/TensorFlow)
- Output: plots comparing true vs predicted prices

## How to run (locally)
1. Create & activate virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1

2. Install dependencies:

pip install -r requirements.txt

3. Run notebook:

jupyter notebook stock_price_prediction.ipynb

### Notes

This is an educational demo, not financial advice.

If you have GPU/large TF requirements, install a suitable TensorFlow build.