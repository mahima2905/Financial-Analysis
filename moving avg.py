import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV
file_path = "C:/Users/Mahima kumari/Downloads/deloitte_financial_data_10yrs.csv"
df = pd.read_csv(file_path)

# Make sure Date is in datetime format and sorted
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Set date as index for rolling
df.set_index('Date', inplace=True)

# 🧮 3-month and 6-month moving averages
df['Revenue_MA_3'] = df['Revenue'].rolling(window=3).mean()
df['Revenue_MA_6'] = df['Revenue'].rolling(window=6).mean()

df['Expenses_MA_3'] = df['Expenses'].rolling(window=3).mean()
df['Expenses_MA_6'] = df['Expenses'].rolling(window=6).mean()

plt.figure(figsize=(14, 6))

# Plot Revenue and its moving averages
plt.plot(df.index, df['Revenue'], label='📈 Revenue', color='blue', linewidth=1.5)
plt.plot(df.index, df['Revenue_MA_3'], label='green 3-Month MA', linestyle='--')
plt.plot(df.index, df['Revenue_MA_6'], label='orange 6-Month MA', linestyle='--')

plt.title('Revenue with 3-Month and 6-Month Moving Averages')
plt.xlabel('Date')
plt.ylabel('Amount (₹)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

