#GROUP BY YEAR
import pandas as pd

# Load the CSV
file_path = "C:/Users/Mahima kumari/Downloads/deloitte_financial_data_10yrs.csv"
df = pd.read_csv(file_path)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract year and group
df['Year'] = df['Date'].dt.year
yearly_totals = df.groupby('Year')[['Revenue', 'Expenses']].sum().reset_index()

print(yearly_totals)


#GROUP BY QUARTER

# Extract quarter
df['Quarter'] = df['Date'].dt.to_period('Q')
quarterly_totals = df.groupby('Quarter')[['Revenue', 'Expenses']].sum().reset_index()

print(quarterly_totals)


#TOTAL PROFIT

# Add Profit column
df['Profit'] = df['Revenue'] - df['Expenses']

# Calculate total profit
total_profit = df['Profit'].sum()

print(f"🧮 Total Profit over 10 years: ₹{total_profit:,.2f}")

# Bar Chart for Yearly Revenue vs Expenses
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.bar(yearly_totals['Year'] - 0.2, yearly_totals['Revenue'], width=0.4, label='Revenue', color='skyblue')
plt.bar(yearly_totals['Year'] + 0.2, yearly_totals['Expenses'], width=0.4, label='Expenses', color='salmon')
plt.title('Yearly Revenue vs Expenses')
plt.xlabel('Year')
plt.ylabel('Amount (₹)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

#PIE CHART FOR TOTAL REVENUE AND EXPENCES

# Total values
totals = [df['Revenue'].sum(), df['Expenses'].sum()]
labels = ['Revenue', 'Expenses']
colors = ['lightgreen', 'lightcoral']

plt.figure(figsize=(6, 6))
plt.pie(totals, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Total Revenue vs Expenses (10 Years)')
plt.tight_layout()
plt.show()

