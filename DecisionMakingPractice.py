# Import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Data (text, label)
data = [
    ("hello", 1),
    ("hi", 1),
    ("hey", 1),
    ("greetings", 1),
    ("good morning", 1),
    ("how are you", 0),
    ("what's the time", 0),
    ("weather", 0),
    ("bye", 0),
    ("see you later", 0)
]

# Separate input text and labels
X = [text for text, label in data]
y = [label for text, label in data]

# Convert text to numeric features using Bag of Words
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train a classifier (Logistic Regression in this case)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Function to predict if input is a greeting
def is_greeting(text):
    text_vectorized = vectorizer.transform([text])
    prediction = classifier.predict(text_vectorized)
    return prediction[0]  # 1 for greeting, 0 for non-greeting

# Testing the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    if is_greeting(user_input):
        print("Chatbot: Hello! How can I help you?")
    else:
        print("Chatbot: I'm not sure what you're asking.")
