from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)

CORS(app)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({'locations': util.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.form
    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])
    
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    
    response = jsonify({'estimated_price': estimated_price})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    print("Starting Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True, host="0.0.0.0", port=5000)
