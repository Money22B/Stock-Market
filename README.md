Stock Market Predictor (Streamlit + LSTM)

This project is a Stock Market Prediction Web App built using Streamlit and a trained LSTM (Deep Learning) model. It fetches real-time stock data, visualizes trends, and predicts future stock prices.

---

Features

- Fetch real-time stock data using Yahoo Finance
- Visualize stock price trends
- Moving Averages:
  - MA50
  - MA100
  - MA200
- Predict stock prices using LSTM model
- Forecast next 30 days of stock prices
- Download predictions as CSV

---

Technologies Used

- Python
- Streamlit
- TensorFlow / Keras
- NumPy & Pandas
- Matplotlib
- yFinance
- Scikit-learn

---

Project Structure

├── app.py                # Main Streamlit application
├── stock8.keras         # Trained LSTM model
├── README.md            # Project documentation

---

 Installation & Setup

1. Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install dependencies
numpy
pandas
yfinance
tensorflow
matplotlib
streamlit
scikit-learn

pip install -r requirements.txt

4. Run the app

streamlit run app.py

---

Usage

1. Enter a stock symbol (e.g., "AAPL", "TSLA", "RELIANCE")
2. View:
   - Historical stock data
   - Moving averages graphs
   - Predicted vs actual prices
3. Check future 30-day predictions
4. Download results as CSV

---

Model Details

- Model Type: LSTM (Long Short-Term Memory)
- Input: Last 100 days stock prices
- Output: Next price prediction
- Scaling: MinMaxScaler

---

Important Notes

- The model file path in code should be updated:

model = load_model('stock8.keras')

- Current path is local:

C:\\Users\\Yashpal Singh\\Downloads\\stock8.keras

- Make sure the model file is in your project folder.

---

Screenshots (Optional)

Add screenshots of your app here

---

Future Improvements

- Add multiple stock comparison
- Improve prediction accuracy
- Deploy on cloud (Streamlit Cloud / Render)
- Add news sentiment analysis

---

Contributing

Feel free to fork this repository and contribute!

---

License

This project is open-source and free to use.

---

Author

Your Name

---

 If you like this project, give it a star on GitHub!
