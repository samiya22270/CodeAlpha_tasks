# Task 2 - Exploratory Data Analysis (EDA)

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv("books_data.csv")

# Display First 5 Rows
print("First 5 Rows:\n")
print(data.head())

# Dataset Information
print("\nDataset Information:\n")
print(data.info())

# Check Missing Values
print("\nMissing Values:\n")
print(data.isnull().sum())

# Statistical Summary
print("\nStatistical Summary:\n")
print(data.describe())

# Count of Ratings
print("\nRatings Count:\n")
print(data["Rating"].value_counts())

# Visualization - Rating Distribution
plt.figure(figsize=(8,5))
sns.countplot(x=data["Rating"])

plt.title("Book Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Count")

plt.show()

# Convert Price Column to Numeric
data["Price"] = data["Price"].replace("£", "", regex=True).astype(float)

# Visualization - Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(data["Price"], bins=10)

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()

print("\nEDA Completed Successfully!")
