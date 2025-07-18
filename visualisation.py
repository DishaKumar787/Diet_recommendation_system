# -*- coding: utf-8 -*-
"""Visualisation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LguhVaJahINX6-2eHV_GOq4yAXSKZ50x
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset from CSV file
file_path = '/content/sample_data/NEWFOOD.csv'
encodings = ['utf-8', 'latin1', 'cp1252']
for encoding in encodings:
    try:
        data = pd.read_csv(file_path, encoding=encoding)
        break
    except UnicodeDecodeError:
        print(f"Failed to decode with encoding {encoding}, trying next...")

# Ensure the CSV file has the required columns
expected_columns = ['sno.', 'name', 'cuisine', 'course', 'diet', 'price']
data.columns = data.columns.str.strip()  # Remove any leading/trailing whitespace from column names

if not all(column in data.columns for column in expected_columns):
    print("Columns in the dataset:", data.columns.tolist())
    raise ValueError(f"The CSV file must contain the following columns: {expected_columns}")

data['price'] = data['price'].str.replace('[^\d.]', '', regex=True)  # Remove non-numeric characters
data['price'] = data['price'].replace('', '0')  # Handle any remaining empty strings
data['price'] = data['price'].astype(float)  # Convert to float

def create_bar_graph(x, y, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='skyblue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Number of dishes by course
course_count = data['course'].value_counts()
create_bar_graph(course_count.index, course_count.values, 'Course', 'Number of Dishes', 'Number of Dishes by Course')

# Number of dishes by diet
diet_count = data['diet'].value_counts()
create_bar_graph(diet_count.index, diet_count.values, 'Diet', 'Number of Dishes', 'Number of Dishes by Diet')

# Number of dishes by price range
price_bins = [0, 10, 20, 30, 40, 50, 100, 200]
price_labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-100', '100-200']
data['price_range'] = pd.cut(data['price'], bins=price_bins, labels=price_labels)
price_count = data['price_range'].value_counts().sort_index()
create_bar_graph(price_count.index, price_count.values, 'Price Range ($)', 'Number of Dishes', 'Number of Dishes by Price Range')