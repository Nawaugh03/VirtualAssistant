from flask import Blueprint, request, jsonify
from .utils import predict_label

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome home!"})

@main.route('/predict', method=['POST'])
def predict():
    data=request.get_json()
    result=predict_label(data['text'])
    return jsonify({"prediction": result})
