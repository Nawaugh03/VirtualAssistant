import joblib

# Load model and vectorizer at the start (to avoid reloading with each request)
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_label(text):
    transformed_text = vectorizer.transform([text])
    prediction = model.predict(transformed_text)
    labels = {0: "Greetings", 1: "Goodbye", 2: "Task request", 3: "Casual talk"}
    return labels.get(prediction[0], "Unknown")
