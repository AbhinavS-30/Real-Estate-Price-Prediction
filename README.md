# Real Estate Price Prediction

## About The Project
This is a machine learning-powered real estate price prediction web app built using:
- Python (Flask)
- Scikit-Learn
- Pandas & NumPy
- JavaScript (jQuery)
- HTML & CSS

# Dataset Source- Kaggle
# Dataset Link- https://www.kaggle.com/datasets/rachitchourasia/bangaluru-house-price-data

It allows users to predict house prices based on:
- Location
- Square Footage
- Number of BHKs
- Number of Bathrooms

## Installation & Setup

### Run the following commands in your terminal:


# Step 1: Clone the Repository
git clone https://github.com/AbhinavS-30/Real-Estate-Price-Prediction.git
cd Real-Estate-Price-Prediction

# Step 2: Install Dependencies
pip install -r requirements.txt

# Step 3: Start the Backend Server
python server/server.py
# If successful, you should see:
# Starting Flask Server for Home Price Prediction...
# * Running on http://127.0.0.1:5000/

# Step 4: Start the Frontend
# Option 1: Using Python’s HTTP Server
cd client
python -m http.server 5500
# Then open: http://127.0.0.1:5500/app.html

# Features
- Predict House Prices using Machine Learning
- Location-based Pricing
- Interactive UI with Dropdown Selection
- Flask API Backend for Predictions
- Frontend using JavaScript, HTML, CSS

# Machine Learning Model
- The model is trained on a Bangalore house price dataset.
- Uses Linear Regression for price prediction.
- Feature Engineering:
- One-Hot Encoding for locations
- Outlier removal & feature scaling
- The trained model is saved using pickle and loaded in the Flask API.

# Project Structure

Real Estate Price Prediction
│── client (Frontend - HTML, CSS, JS)
│   │── app.html
│   │── app.js
│   │── app.css
│
│── server (Backend - Flask API)
│   │── server.py
│   │── util.py
│   │── artifacts
│   │   ├── columns.json
│   │   ├── banglore_home_prices_model.pickle
│
│── dataset
│   │── bengaluru_house_prices.csv
│
│── README.md
│── requirements.txt

# Future Enhancements
- Deploy on Heroku or AWS
- Add more features such as balconies, parking, age of house
- Improve UI with React.js
- Implement a better feature selection strategy for improved accuracy
- Train with more complex models (Decision Trees, XGBoost, etc.)
- Build a better user interface with React.js
