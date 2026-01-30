import pandas as pd

# ---------------- UNIT 5 : ADVANCED PANDAS ----------------

# Sample data
data = {
    "Date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "Sales": [120, 150, 170, 160, 180, 200, 210, 190, 220, 230],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West", "North", "South"]
}

df = pd.DataFrame(data)

# ---------------- 1. DateTime Handling ----------------
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# ---------------- 2. Time Series Resampling ----------------
daily_sales = df.resample("D").sum()
weekly_sales = df.resample("W").mean()

# ---------------- 3. Rolling Window Operations ----------------
df["Rolling_Avg_3"] = df["Sales"].rolling(window=3).mean()

# ---------------- 4. Expanding Operations ----------------
df["Cumulative_Avg"] = df["Sales"].expanding().mean()

# ---------------- 5. Shift & Difference ----------------
df["Previous_Day_Sales"] = df["Sales"].shift(1)
df["Sales_Change"] = df["Sales"].diff()

# ---------------- 6. Data Reshaping ----------------
long_format = df.reset_index().melt(
    id_vars=["Date"],
    value_vars=["Sales", "Rolling_Avg_3"],
    var_name="Metric",
    value_name="Value"
)

# ---------------- 7. Stack & Unstack ----------------
stacked_df = df[["Sales", "Rolling_Avg_3"]].stack()
unstacked_df = stacked_df.unstack()

# ---------------- 8. Categorical Data ----------------
df["Region"] = df["Region"].astype("category")

# ---------------- Output ----------------
print("Final DataFrame:\n", df)
print("\nWeekly Sales:\n", weekly_sales)
print("\nLong Format Data:\n", long_format)
print("\nStacked Data:\n", stacked_df)
