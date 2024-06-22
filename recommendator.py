import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
file_path = '7817_1.csv'
data = pd.read_csv(file_path)

# Strip any leading/trailing spaces from the column names
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

# Create the user-item interaction matrix
user_item_matrix = data.pivot_table(index='UserId', columns='ProductId', values='Rating')

# Fill NaN values with 0 to compute similarity
user_item_matrix_filled = user_item_matrix.fillna(0)

# Compute cosine similarity between items
item_similarity_matrix = cosine_similarity(user_item_matrix_filled.T)

# Convert to DataFrame for easier manipulation
item_similarity_df = pd.DataFrame(item_similarity_matrix, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# Function to get recommendations
def get_recommendations(user_id, user_item_matrix, item_similarity_df, n_recommendations=5):
    # Get the products rated by the user
    user_ratings = user_item_matrix.loc[user_id].dropna()
    
    # Initialize a dictionary to store recommendation scores
    recommendation_scores = {}
    
    # Iterate over each product rated by the user
    for product, rating in user_ratings.items():
        # Get the list of similar products
        similar_products = item_similarity_df[product]
        
        # Compute the recommendation score for each similar product
        for similar_product, similarity in similar_products.items():
            if similar_product in user_ratings.index:
                continue
            if similar_product not in recommendation_scores:
                recommendation_scores[similar_product] = similarity * rating
            else:
                recommendation_scores[similar_product] += similarity * rating
    
    # Sort the products by recommendation score
    recommended_products = sorted(recommendation_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Get the top N recommended products
    recommended_products = [product for product, score in recommended_products[:n_recommendations]]
    
    return recommended_products

# Display all customers with a number for selection
unique_users = data['UserId'].unique()
print("Select a customer to get recommendations:")
for idx, user in enumerate(unique_users):
    print(f"{idx}: {user}")

# Get user input to select a customer
user_idx = int(input("Enter the number corresponding to the customer: "))
selected_user_id = unique_users[user_idx]

# Get recommendations for the selected customer
recommended_products = get_recommendations(selected_user_id, user_item_matrix, item_similarity_df)
print(f"Recommended products for user {selected_user_id}: {recommended_products}")
