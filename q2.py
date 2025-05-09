import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download and save the CSV
ticker = "AMZN"
url = f"https://raw.githubusercontent.com/itb-ie/midterm_data/refs/heads/main/{ticker}.csv"
with open("company.csv", "w") as f:
    f.write(requests.get(url).text)

# Step 2: Load the data
df = pd.read_csv("company.csv", index_col="Date")

# Step 3: Convert the index to datetime
df.index = pd.to_datetime(df.index)

# Question 1
print("Number of rows:")
print(len(df))

print("\nColumn names:")
print(df.columns)

print("\nLowest stock value on April 10th:")
print(df.loc["2025-04-10", "Low"])  # assuming date format is YYYY-MM-DD

# Question 2: Plot a column (e.g., 'Close')
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Close"], label="Close Price")
plt.title("AMZN Stock - Close Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.grid(True)
plt.legend()
plt.show()
