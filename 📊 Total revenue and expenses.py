import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# Load the CSV file
df= pd.read_csv("C:/Users/Mahima kumari/Downloads/deloitte_financial_data_10yrs.csv")

# Calculate total revenue and total expenses
total_revenue = df['Revenue'].sum()
total_expenses = df['Expenses'].sum()

# Display the results
print(f" Total Revenue over 10 years: ₹{total_revenue:,.2f}")
print(f" Total Expenses over 10 years: ₹{total_expenses:,.2f}")
