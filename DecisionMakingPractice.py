# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression

df= pd.read_csv("PracticeDataset.csv")

vectorizer = TfidfVectorizer(stop_words='english')  # Adding stop words removal for cleaner data
X=vectorizer.fit_transform(df['text'])
y=df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model =LogisticRegression()

model.fit(X_train, y_train)

# Check the accuracy on the test set
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

#Using Cross-Validation to get More reliable performance estimate
cv_scores=cross_val_score(model,X,y, cv=5) #5-fold cross-validation
print(f"Cross-validation Accuracy: {cv_scores.mean()*100:.2f}%")

# Example new input
new_input = ["ja ja ja"]

# Convert the new input to the same feature space as training data
new_input_transformed = vectorizer.transform(new_input)

# Predict using the trained model
prediction = model.predict(new_input_transformed)

# Output the result
if prediction[0] == 0:
    print("Greetings")
elif (prediction[0]==1):
    print("Saying goodbye")
elif(prediction[0]==2):
    print("Understand a Task performance")
elif (prediction[0]==3):
    print("Casually talking")
else:
    print("Unknown imput")

probas= model.predict_proba(new_input_transformed)
print(f"Prediction confidence: {max(probas[0]) * 100:.2f}%")
