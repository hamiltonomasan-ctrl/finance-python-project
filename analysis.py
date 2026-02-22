import pandas as pd
import matplotlib.pyplot as plt

# Load your Excel file
df = pd.read_excel("data/spending.xlsx")

# Clean column names (important)
df.columns = df.columns.str.strip()

# --- Basic checks ---
print("First 5 rows:")
print(df.head())

# --- Total spending ---
total = df["Amount ($)"].sum()
print("\nTotal Spending:", total)

# --- Spending by category ---
category_totals = (
    df.groupby("Category")["Amount ($)"]
      .sum()
      .sort_values(ascending=False)
)

print("\nSpending by Category:")
print(category_totals)

# --- Pie chart: spending breakdown ---
plt.figure()
category_totals.plot(kind="pie", autopct="%1.1f%%")
plt.title("Spending Breakdown by Category")
plt.ylabel("")  # hide y-label
plt.tight_layout()
plt.show()

# --- Daily trend ---
df["Date"] = pd.to_datetime(df["Date"])
daily_totals = df.groupby("Date")["Amount ($)"].sum()

plt.figure()
daily_totals.plot(kind="line", marker="o")
plt.title("Daily Spending Trend")
plt.xlabel("Date")
plt.ylabel("Amount ($)")
plt.tight_layout()
plt.show()
