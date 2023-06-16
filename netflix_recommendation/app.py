from datetime import datetime
import json
from pathlib import Path
import pickle
from flask import Flask, render_template, request, jsonify
import numpy as np
import requests

def recommend_products(rules_df, product_id, rec_count=7):
    sorted_rules = rules_df.sort_values('lift', ascending=False)
    recommended_products = []

    for i, product in sorted_rules["antecedents"].items():
        for j in list(product):
            if j == product_id:
                # Check if product_id is not in the consequents list
                if product_id not in sorted_rules.iloc[i]["consequents"]:
                    recommended_products.append(
                        list(sorted_rules.iloc[i]["consequents"]))

    recommended_products = list({item for item_list in recommended_products for item in item_list})

    return recommended_products[:rec_count]

def get_golden_shot(target_id, rules):
    recommended_product_ids = recommend_products(rules, target_id)
    return recommended_product_ids

app = Flask(__name__)

# Load the saved model
loaded_model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    # Get user input from the request
    user_input = request.json

    # Perform necessary data preprocessing and feature engineering on user_input
    # Make predictions using the loaded model
    recommendations = loaded_model.predict(user_input)

    # Render the result.html template with the recommendations
    return render_template('result.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
