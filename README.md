# Real Estate Price Prediction

## About The Project
This is a machine learning-powered real estate price prediction web app built using:
- Python (Flask)
- Scikit-Learn
- Pandas & NumPy
- JavaScript (jQuery)
- HTML & CSS

## Dataset Source- Kaggle
## Dataset Link- https://www.kaggle.com/datasets/rachitchourasia/bangaluru-house-price-data

It allows users to predict house prices based on:
- Location
- Square Footage
- Number of BHKs
- Number of Bathrooms

## Installation & Setup

### Run the following commands in your terminal:


## Step 1: Clone the Repository
git clone https://github.com/AbhinavS-30/Real-Estate-Price-Prediction.git

## Step 2: Start the Backend Server (Run in server)
python server/server.py

## Step 3: Start the Frontend (Run in client)
python -m http.server 5500
## Then open: http://127.0.0.1:5500/app.html in browser

## Features
- Predict House Prices using Machine Learning
- Location-based Pricing
- Interactive UI with Dropdown Selection
- Flask API Backend for Predictions
- Frontend using JavaScript, HTML, CSS

## Machine Learning Model
- The model is trained on a Bangalore house price dataset.
- Uses Linear Regression for price prediction.
- Feature Engineering:
- One-Hot Encoding for locations
- Outlier removal & feature scaling
- The trained model is saved using pickle and loaded in the Flask API.

## Future Enhancements
- Deploy on Heroku or AWS
- Add more features such as balconies, parking, age of house
- Improve UI with React.js
- Implement a better feature selection strategy for improved accuracy
- Train with more complex models (Decision Trees, XGBoost, etc.)
- Build a better user interface with React.js

## License
### MIT License - Free to use and modify.


