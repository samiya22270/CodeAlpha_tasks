# Task 3 - Data Visualization

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv("books_data.csv")

# Convert Price Column to Numeric
data["Price"] = data["Price"].replace("£", "", regex=True).astype(float)

# -----------------------------
# 1. Rating Distribution Chart
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x=data["Rating"])

plt.title("Book Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Number of Books")

plt.show()

# -----------------------------
# 2. Price Distribution Histogram
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(data["Price"], bins=10)

plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()

# -----------------------------
# 3. Price vs Rating Boxplot
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x=data["Rating"], y=data["Price"])

plt.title("Price vs Rating")
plt.xlabel("Ratings")
plt.ylabel("Price")

plt.show()

print("Data Visualization Completed Successfully!")
