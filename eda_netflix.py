

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic Information
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Content Type Distribution
print("\nType Distribution:")
print(df['type'].value_counts())

# Top Countries
print("\nTop Countries:")
print(df['country'].value_counts().head(10))

# Ratings Distribution
print("\nRatings:")
print(df['rating'].value_counts())
df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()
df['country'].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.show()
df['release_year'].value_counts().sort_index().plot()

plt.title("Content Release Trend")
plt.xlabel("Year")
plt.ylabel("Number of Titles")

plt.show()