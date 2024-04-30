from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
app = Flask(__name__)
CORS(app)

# Load the machine learning model
model = pickle.load(open(r'C:\Users\thejan\Downloads\navbar\RandomF_model.pkl', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    age = data['age']
    al = data['al']
    su = data['su']
    bgr = data['bgr']
    bu = data['bu']
    sc = data['sc']
    sod = data['sod']
    pcv = data['pcv']
    rc = data['rc']
    htn = data['htn'] 

    # Convert 'htn' to binary (0 or 1)
    htn_binary = 1 if htn == 'yes' else 0

    # Predict using the model
    prediction = model.predict([[age, al, su, bgr, bu, sc, sod, pcv, rc, htn_binary]])

    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
