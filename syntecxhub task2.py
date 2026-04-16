#Step1: ImportLibraries
import pandas as pd
import numpy as np

#Step 2:Read CSV File
# Load dataset
df = pd.read_csv("data.csv")

# Display first rows
print(df.head())

# Display last rows
print(df.tail())

# Data types
print(df.dtypes)

#Step 3: Summary Statistics
print("Mean:\n", df.mean(numeric_only=True))
print("Median:\n", df.median(numeric_only=True))
print("Minimum:\n", df.min(numeric_only=True))
print("Maximum:\n", df.max(numeric_only=True))
print("Count:\n", df.count())

#Step 4: Select Columns
# Select specific column
print(df["Age"])

# Multiple columns
print(df[["Name", "Age"]])

#Step 5: Filter Rows
# Filter rows where Age > 25
filtered = df[df["Age"] > 25]
print(filtered)

#Step 6: Slice Subset
subset = df.iloc[0:5, 0:3]
print(subset)

#Step 7: Save Filtered Results
filtered.to_csv("filtered_data.csv", index=False)

