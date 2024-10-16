from flask import Blueprint, request, jsonify
#from .utils import predict_label

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome home!"})

@main.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@main.route('/info')
def info():
    return jsonify({"info": "This is a simple Flask API"})
#@main.route('/predict', method=['POST'])
#def predict():
#    data=request.get_json()
#    result=predict_label(data['text'])
#    return jsonify({"prediction": result})
