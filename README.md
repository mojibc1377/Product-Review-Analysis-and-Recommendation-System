# Product-Review-Analysis-and-Recommendation-System
# E-commerce Product Review Analysis

## Overview

This script (`analysis.py`) is responsible for loading, cleaning, and exploring the product review dataset. The main objectives are to understand the distribution of ratings, user activity, product popularity, and identify the most liked and least liked products.

## Steps

1. **Data Loading and Cleaning**:
   - Load the dataset from a CSV file.
   - Clean the column names and handle missing values and duplicates.
   - Select relevant columns and convert date columns to datetime format.

2. **Exploratory Data Analysis (EDA)**:
   - Visualize the distribution of ratings.
   - Analyze user activity by plotting the number of ratings per user.
   - Analyze product popularity by plotting the number of ratings per product.
   - Identify the most liked and least liked products based on average ratings.

## Key Visualizations

### 1. Distribution of Ratings
This bar chart shows the frequency of each rating value. It helps in understanding the overall sentiment of the users towards the products. Higher ratings indicate more positive feedback.

![Distribution of Ratings](./path/to/your/image1.png)

### 2. User Activity Distribution
This histogram displays the number of ratings per user. It helps in identifying how active the users are in rating the products. Most users have rated very few products, with a few users being extremely active.

![User Activity Distribution](./path/to/your/image2.png)

### 3. Product Popularity Distribution
This histogram displays the number of ratings per product. It helps in identifying which products are rated the most. Most products have a few ratings, with a few products being very popular.

![Product Popularity Distribution](./path/to/your/image3.png)

### 4. Top 10 Most Liked Products
This bar chart shows the top 10 products with the highest average ratings. It helps in identifying the most liked products by the users.

![Top 10 Most Liked Products](./path/to/your/image4.png)

### 5. Top 10 Least Liked Products
This bar chart shows the top 10 products with the lowest average ratings. It helps in identifying the least liked products by the users.

![Top 10 Least Liked Products](./path/to/your/image5.png)

## How to Run

1. **Install the required libraries**:
   ```bash
   pip install pandas matplotlib seaborn

### README for `recommendator.py`

```markdown
# E-commerce Product Recommendation System

## Overview

The recommendation script (`recommendator.py`) is responsible for generating product recommendations for users based on their past ratings. The main objective is to recommend products that a user might like but has not rated yet.

## Steps

1. **Data Loading and Cleaning**:
   - Load the dataset from a CSV file.
   - Clean the column names and handle missing values and duplicates.
   - Select relevant columns and convert date columns to datetime format.

2. **User-Item Interaction Matrix**:
   - Create a matrix where rows represent users, columns represent products, and values are ratings.

3. **Item Similarity**:
   - Compute cosine similarity between items based on user ratings.

4. **Generate Recommendations**:
   - For a selected user, recommend products based on similarity to products they have rated.

## How to Run

1. **Install the required libraries**:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
