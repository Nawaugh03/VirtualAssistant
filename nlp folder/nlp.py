import pandas as pd
import os
import re
import nltk
import matplotlib
from nltk.corpus  import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

#nltk.download()
directory="nlp folder"
filename="test.txt"
file_path=os.path.join(directory,filename)
data = pd.read_csv(file_path, sep=";", header=None, names=["text", "label"])

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stopwords.words("english")])
    return text

data["text"] = data["text"].apply(preprocess_text)
if __name__=='__main__':
    #print(os.getcwd())
    #print(data.head())
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data["text"])
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(class_weight='balanced',n_estimators=200, random_state=42, max_depth=20)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
    new_phrase=["I'm ok"]
    X_new = vectorizer.transform(new_phrase)
    prediction=model.predict(X_new)
    print("Prediction Label:",prediction[0])

    prediction_proba = model.predict_proba(X_new)
    print("Prediction probabilities:", prediction_proba)
