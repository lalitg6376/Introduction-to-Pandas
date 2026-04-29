import pandas as pd
import numpy as np

# ------------------ UNIT 6 : REAL WORLD PANDAS PROJECT ----------------

# Sample employee dataset
data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Age": [23, 29, 35, 41, 28, 39, 31, 26],
    "Experience": [1, 5, 10, 15, 4, 12, 7, 2],
    "Salary": [30000, 45000, 70000, 90000, 42000, 85000, 65000, 38000],
    "Performance": [3.2, 4.1, 4.8, 3.9, 4.0, 4.6, 4.3, 3.5]
}

df = pd.DataFrame(data)

# ---------------- 1. Department Wise Analysis ----------------
dept_summary = df.groupby("Department").agg(
    Avg_Salary=("Salary", "mean"),
    Max_Salary=("Salary", "max"),
    Avg_Experience=("Experience", "mean"),
    Employee_Count=("Emp_ID", "count")
)

# ---------------- 2. Employee Ranking ----------------
df["Salary_Rank"] = df["Salary"].rank(ascending=False, method="dense")
df["Performance_Rank"] = df["Performance"].rank(ascending=False)

# ---------------- 3. High & Low Salary Classification ----------------
salary_q1 = df["Salary"].quantile(0.25)
salary_q3 = df["Salary"].quantile(0.75)

df["Salary_Level"] = pd.cut(
    df["Salary"],
    bins=[0, salary_q1, salary_q3, df["Salary"].max()],
    labels=["Low", "Medium", "High"]
)

# ---------------- 4. Experience Based Flag ----------------
df["Senior_Employee"] = df["Experience"] >= 8

# ---------------- 5. Department Performance Score ----------------
dept_performance = df.groupby("Department")["Performance"].mean()

# ---------------- 6. Sorting for Business Insight ----------------
top_paid = df.sort_values(by="Salary", ascending=False).head(5)

# ---------------- 7. Memory Optimization ----------------
df["Department"] = df["Department"].astype("category")

# ---------------- Output --------------
print("Employee Data:\n", df)
print("\nDepartment Summary:\n", dept_summary)
print("\nDepartment Performance Score:\n", dept_performance)
print("\nTop Paid Employees:\n", top_paid)
