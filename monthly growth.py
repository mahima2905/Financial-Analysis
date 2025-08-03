import pandas as pd
import matplotlib.pyplot as plt

#READ DATA
df = pd.read_csv("C:/Users/Mahima kumari/Downloads/deloitte_financial_data_10yrs.csv")

# Convert Date to datetime format
df['Date'] = pd.to_datetime(df['Date'])

df = df.sort_values('Date')  # sort by date

# Set Date as index (monthly frequency)
df.set_index('Date', inplace=True)
df = df.resample('M').sum()  # ensure data is monthly

# 🧮 Calculate Monthly Growth Rate (%)
df['Revenue Growth %'] = df['Revenue'].pct_change() * 100
df['Expenses Growth %'] = df['Expenses'].pct_change() * 100

# 🎯 Plotting the Growth Rates
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Revenue Growth %'], marker='o', label='📈 Revenue Growth %')
plt.plot(df.index, df['Expenses Growth %'], marker='o', label='📉 Expenses Growth %')

plt.axhline(0, color='gray', linestyle='--', linewidth=0.7)
plt.title('Monthly Growth Rate of Revenue and Expenses')
plt.xlabel('Month')
plt.ylabel('Growth Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


#CAGR (Compound Annual Growth Rate) 

import pandas as pd

# Assuming df has 'Date', 'Revenue', and 'Expenses' columns
df['Date'] = pd.to_datetime(df['Date'])

# Sort by Date just to be sure
df = df.sort_values('Date')

# Get start and end values
start_date = df['Date'].min()
end_date = df['Date'].max()

start_revenue = df[df['Date'] == start_date]['Revenue'].values[0]
end_revenue = df[df['Date'] == end_date]['Revenue'].values[0]

start_expenses = df[df['Date'] == start_date]['Expenses'].values[0]
end_expenses = df[df['Date'] == end_date]['Expenses'].values[0]

# Calculate number of years
num_years = (end_date - start_date).days / 365.25

# Calculate CAGR
cagr_revenue = ((end_revenue / start_revenue) ** (1 / num_years)) - 1
cagr_expenses = ((end_expenses / start_expenses) ** (1 / num_years)) - 1

# Print results
print(f"📈 CAGR of Revenue: {cagr_revenue * 100:.2f}%")
print(f"📉 CAGR of Expenses: {cagr_expenses * 100:.2f}%")

