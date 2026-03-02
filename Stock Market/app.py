import numpy as np
import pandas as pd
import yfinance as yf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import streamlit as st
import os

os.makedirs("stock app", exist_ok=True)

print(os.listdir("stock app"))

model = load_model(r'C:\Users\Yashpal Singh\Downloads\stock8.keras')

st.header('Stock Market Predictor')

stock = st.text_input('Enter Stock Symnbol','AAPL')
start = '2012-01-01'
end = '2025-10-17'

data = yf.download(stock, start ,end)

data = data.reset_index()

st.subheader('Stock Data')
st.write(data)

data_train = pd.DataFrame(data.Close[0: int(len(data)*0.80)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

pas_100_days = data_train.tail(100)
data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
data_test_scale = scaler.fit_transform(data_test)



st.subheader('Price vs MA50')
ma_50_days = data.Close.rolling(50).mean()
fig1= plt.figure(figsize=(10,8))
plt.plot(ma_50_days,'r')
plt.plot(data.Close,'g')
plt.show()
st.pyplot(fig1)

st.subheader('Price vs MA50 vs MA100')
ma_100_days = data.Close.rolling(100).mean()
fig2= plt.figure(figsize=(10,8))
plt.plot(ma_50_days,'r')
plt.plot(ma_100_days,'b')
plt.plot(data.Close,'g')
plt.show()
st.pyplot(fig2)

st.subheader('Price vs MA50 vs MA100 vs MA200')
ma_200_days = data.Close.rolling(200).mean()
fig3= plt.figure(figsize=(10,8))
plt.plot(ma_50_days,'r')
plt.plot(ma_100_days,'b')
plt.plot(ma_200_days,'y')
plt.plot(data.Close,'g')
plt.show()
st.pyplot(fig3)

x = []
y = []
for i in range(100, data_test_scale.shape[0]):
    x.append(data_test_scale[i-100:i])
    y.append(data_test_scale[i,0])
x, y = np.array(x), np.array(y)

y_predict = model.predict(x)

1/scaler.scale_

y_predict = y_predict*(1/scaler.scale_)

y = y*(1/scaler.scale_)

st.subheader('Original Price vs Predicted Price')
fig4= plt.figure(figsize=(10,8))
plt.plot(y_predict,'r',label='Original Price')
plt.plot(y,'g',label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.show()
st.pyplot(fig4)

st.subheader("Predict Next 30 Days")

scaler.fit(np.array(data["Close"]).reshape(-1, 1))
last_100_days = data["Close"][-100:].values
last_100_days_scaled = scaler.transform(last_100_days.reshape(-1, 1))

future_input = list(last_100_days_scaled.flatten())
future_output = []

for i in range(30):
    x_input = np.array(future_input[-100:]).reshape(1, 100, 1)
    next_pred = model.predict(x_input, verbose=0)
    future_output.append(next_pred[0][0])
    future_input.append(next_pred[0][0])

future_output = np.array(future_output).reshape(-1, 1)
future_predicted = scaler.inverse_transform(future_output)

future_dates = pd.date_range(start=data["Date"].iloc[-1] + pd.Timedelta(days=1), periods=30)

future_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted_Close": future_predicted.flatten()
})


fig5 = plt.figure(figsize=(10, 6))
plt.plot(data["Date"], data["Close"], label="Historical Data", color="blue")
plt.plot(future_df["Date"], future_df["Predicted_Close"], "r--", label="Future Prediction (30 Days)")
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title(f"Stock Price Forecast for Next 30 Days: {stock}")
plt.legend()
st.pyplot(fig5)

st.write("📅 Future 30-Day Predicted Prices:")
st.dataframe(future_df)

csv = future_df.to_csv(index=False).encode("utf-8")
st.download_button("Download Future Predictions as CSV", data=csv, file_name=f"{stock}_future_30days.csv", mime="text/csv")

