import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

#READ DATA
df = pd.read_csv("C:/Users/Mahima kumari/Downloads/deloitte_financial_data_10yrs.csv")

#  Prepare your dataset
df['Date'] = pd.to_datetime(df['Date'])

# Replace 'Revenue' with 'Expenses' if you want to forecast that instead
data_prophet = df[['Date', 'Revenue']].rename(columns={'Date': 'ds', 'Revenue': 'y'})

#  Create and fit model
model = Prophet()
model.fit(data_prophet)

#  Create future 12 months (or change 'periods' to 24, 36 for more)
future = model.make_future_dataframe(periods=12, freq='M')

#  Forecast
forecast = model.predict(future)

#  Plot forecast
model.plot(forecast)
plt.title('📈 Revenue Forecast with Trend & Seasonality')
plt.show()

#  Plot components: trend, weekly, yearly seasonality
model.plot_components(forecast)
plt.suptitle('📊 Decomposition: Trend & Seasonality')
plt.show()



