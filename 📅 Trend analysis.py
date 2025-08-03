import pandas as pd
import matplotlib.pyplot as plt

# 👉 If your data is in a CSV
df = pd.read_csv('C:/Users/Mahima kumari/Downloads/deloitte_financial_data_10yrs.csv')
"""
# 📅 Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# 📊 Group or resample monthly (if not already monthly)
df = df.sort_values('Date')
df.set_index('Date', inplace=True)
monthly_expenses = df['expenses'].resample('M').sum()

# 📈 Plot Revenue Trend
plt.figure(figsize=(12, 6))
plt.plot(monthly_expenses .index, monthly_expenses.values, marker='o', color='teal')
plt.title('📅 expenses Trend Over Time')
plt.xlabel('Month')
plt.ylabel('expenses')
plt.grid(True)
plt.tight_layout()
plt.show()"""

#FOR EXPENSES
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Step 1: Convert 'Date' to datetime format (if not already)
df['Date'] = pd.to_datetime(df['Date'])

# ✅ Step 2: Set date as index and resample by month (if data is daily or irregular)
df.set_index('Date', inplace=True)
monthly_expenses = df['Expenses'].resample('M').sum()

# ✅ Step 3: Plot the expense trend
plt.figure(figsize=(12, 6))
plt.plot(monthly_expenses.index, monthly_expenses.values, marker='o', color='tomato', label='Expenses')

plt.title('📅 Trend Analysis: Expenses Over Time')
plt.xlabel('Month')
plt.ylabel('Expenses')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
