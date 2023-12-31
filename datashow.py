'''
Description about Example:

This Streamlit code showcases a machine learning model's predictions on the Iris dataset. It loads 
the Iris dataset, trains a Random Forest classifier on it, and then allows users to input sepal and 
petal measurements via sliders. The code then uses the trained model to predict the class of the iris 
flower based on the user's input and displays the predicted class, demonstrating a simple interactive 
machine learning application.
'''

import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("Machine Learning Model Showcase")

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a Random Forest classifier
clf = RandomForestClassifier()
clf.fit(X, y)

# User input for prediction
sepal_length = st.slider("Enter sepal length (cm):", 4.0, 7.9, 5.0)
sepal_width = st.slider("Enter sepal width (cm):", 2.0, 4.4, 3.0)
petal_length = st.slider("Enter petal length (cm):", 1.0, 6.9, 4.0)
petal_width = st.slider("Enter petal width (cm):", 0.1, 2.5, 1.3)

# Make predictions
prediction = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])

# Display the predicted class
st.write(f"Predicted class: {iris.target_names[prediction[0]]}")