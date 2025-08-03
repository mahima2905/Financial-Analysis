#Min, Max, Std Dev Calculation

import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/Mahima kumari/Downloads/deloitte_financial_data_10yrs.csv")

# Convert 'Date' to datetime just in case
df['Date'] = pd.to_datetime(df['Date'])

# Calculate statistics
stats = {
    'Metric': ['Minimum', 'Maximum', 'Standard Deviation'],
    'Revenue': [
        df['Revenue'].min(),
        df['Revenue'].max(),
        df['Revenue'].std()
    ],
    'Expenses': [
        df['Expenses'].min(),
        df['Expenses'].max(),
        df['Expenses'].std()
    ]
}

# Create DataFrame for easy display
stats_df = pd.DataFrame(stats)

# Round for cleaner output
stats_df[['Revenue', 'Expenses']] = stats_df[['Revenue', 'Expenses']].round(2)

# Show result
print(stats_df)

# Optional: Save to CSV
stats_df.to_csv("revenue_expenses_statistics.csv", index=False)

#VISUALIZATION

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:/Users/Mahima kumari/Downloads/deloitte_financial_data_10yrs.csv"
df = pd.read_csv(file_path)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date']) 

# Histogram of Revenue
plt.figure(figsize=(10, 5))
plt.hist(df['Revenue'], bins=20, color='skyblue', edgecolor='black')
plt.title("📊 Histogram of Revenue")
plt.xlabel("Revenue (₹)")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Histogram of Expenses

plt.figure(figsize=(10, 5))
plt.hist(df['Expenses'], bins=20, color='salmon', edgecolor='black')
plt.title("📊 Histogram of Expenses")
plt.xlabel("Expenses (₹)")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

#Profit Distribution Boxplot 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
file_path = "C:/Users/Mahima kumari/Downloads/deloitte_financial_data_10yrs.csv"
df = pd.read_csv(file_path)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create Profit column
df['Profit'] = df['Revenue'] - df['Expenses']

plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Profit'], color='lightgreen')
plt.title("📦 Boxplot of Monthly Profit (2015–2024)")
plt.xlabel("Profit (₹)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()






