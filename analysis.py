import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '7817_1.csv'
data = pd.read_csv(file_path)

# Print the column names to check for any discrepancies
print("Original column names:", data.columns)

# Strip any leading/trailing spaces from the column names
data.columns = data.columns.str.strip()

# Print the cleaned column names
print("Cleaned column names:", data.columns)

# Data cleaning
data = data.dropna(subset=['reviews.username', 'name', 'reviews.rating'])  # Drop missing values in key columns
data = data.drop_duplicates()  # Drop duplicate rows

# Select relevant columns for the recommendation system
data = data[['reviews.username', 'name', 'reviews.rating', 'reviews.date']]

# Rename columns for easier reference
data.columns = ['UserId', 'ProductId', 'Rating', 'Timestamp']

# Convert Timestamp to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Display the cleaned dataset
print(data.head())

# Save the cleaned data to a new CSV file for further analysis
data.to_csv('cleaned_reviews.csv', index=False)

# # Basic statistics
# print(data.describe())

# # Number of unique users and products
# print(f"Number of unique users: {data['UserId'].nunique()}")
# print(f"Number of unique products: {data['ProductId'].nunique()}")

# Distribution of ratings
plt.figure(figsize=(8, 6))
sns.countplot(x='Rating', data=data)
plt.title('Distribution of Ratings')
plt.show()

# User activity
user_activity = data.groupby('UserId').size()
plt.figure(figsize=(8, 6))
sns.histplot(user_activity, bins=50)
plt.title('User Activity Distribution')
plt.xlabel('Number of Ratings per User')
plt.ylabel('Number of Users')
plt.show()

# Product popularity
product_popularity = data.groupby('ProductId').size()
plt.figure(figsize=(8, 6))
sns.histplot(product_popularity, bins=50)
plt.title('Product Popularity Distribution')
plt.xlabel('Number of Ratings per Product')
plt.ylabel('Number of Products')
plt.show()

file_path = '7817_1.csv'
data = pd.read_csv(file_path)
data.columns = data.columns.str.strip()

# Data cleaning
data = data.dropna(subset=['reviews.username', 'name', 'reviews.rating'])  # Drop missing values in key columns
data = data.drop_duplicates()  # Drop duplicate rows

# Select relevant columns for the recommendation system
data = data[['reviews.username', 'name', 'reviews.rating', 'reviews.date']]

# Rename columns for easier reference
data.columns = ['UserId', 'ProductId', 'Rating', 'Timestamp']

# Convert Timestamp to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
# Calculate average rating for each product
product_ratings = data.groupby('ProductId')['Rating'].mean().reset_index()
product_ratings.columns = ['ProductId', 'AverageRating']

# Sort products by average rating
most_liked_products = product_ratings.sort_values(by='AverageRating', ascending=False).head(10)
least_liked_products = product_ratings.sort_values(by='AverageRating').head(10)

print("Most Liked Products:")
print(most_liked_products)

print("Least Liked Products:")
print(least_liked_products)
plt.figure(figsize=(12, 6))
sns.barplot(x='AverageRating', y='ProductId', data=most_liked_products, palette='viridis')
plt.title('Top 10 Most Liked Products')
plt.xlabel('Average Rating')
plt.ylabel('Product')
plt.show()

# Plot least liked products
plt.figure(figsize=(12, 6))
sns.barplot(x='AverageRating', y='ProductId', data=least_liked_products, palette='magma')
plt.title('Top 10 Least Liked Products')
plt.xlabel('Average Rating')
plt.ylabel('Product')
plt.show()